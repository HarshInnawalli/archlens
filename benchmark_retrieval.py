"""Quantitative benchmark for ArchLens retrieval and reranking.

Prerequisites:
    1. Start Qdrant on http://localhost:6333.
    2. Build the ``archlens`` collection with the ingestion pipeline.

Run:
    py -m benchmark_retrieval
    py -m benchmark_retrieval --repeats 5 --warmup 1 --json benchmark.json
    py -m benchmark_retrieval --no-rerank --label search_only
"""

from __future__ import annotations

import argparse
import json
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from app.ingestion.indexer import COLLECTION_NAME
from app.retrieval.qdrant import get_qdrant_client
from app.retrieval.reranker import rerank
from app.retrieval.search import SearchResult, search


DEFAULT_QUERIES = [
    "Is Redis Pub/Sub suitable for reliable event processing?",
    "How does Kafka provide durable event delivery?",
    "What are the performance considerations for gRPC services?",
    "How does PostgreSQL support high availability and replication?",
    "How does HTTP caching reduce request load?",
    "What are the risks of using Redis as primary storage?",
    "How should a system handle overload in latency-sensitive microservices?",
    "What are the tradeoffs between synchronous and asynchronous communication?",
]


@dataclass(frozen=True)
class QueryBenchmark:
    label: str
    query: str
    reranking_enabled: bool
    repeats: int
    candidates: int
    reranked_results: int
    search_median_ms: float
    search_p95_ms: float
    rerank_median_ms: float | None
    rerank_p95_ms: float | None
    pipeline_median_ms: float
    pipeline_p95_ms: float


def percentile(values: list[float], percentage: float) -> float:
    """Return a linearly interpolated percentile without extra dependencies."""

    if not values:
        raise ValueError("Cannot calculate a percentile from no values.")

    ordered = sorted(values)
    position = (len(ordered) - 1) * percentage
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower

    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def benchmark_query(
    query: str,
    client,
    repeats: int,
    warmup: int,
    retrieval_top_k: int,
    rerank_top_k: int,
    reranking_enabled: bool,
    label: str,
) -> QueryBenchmark:
    """Measure retrieval, reranking, and their sequential pipeline."""

    for _ in range(warmup):
        candidates = search(
            query,
            client=client,
            top_k=retrieval_top_k,
            collection_name=COLLECTION_NAME,
        )
        if reranking_enabled:
            rerank(query, candidates, top_k=rerank_top_k)

    search_times: list[float] = []
    rerank_times: list[float] = []
    pipeline_times: list[float] = []
    candidate_count = 0
    reranked_count = 0

    for _ in range(repeats):
        candidates: list[SearchResult] = []
        reranked: list[SearchResult] = []

        started = time.perf_counter()
        search_started = time.perf_counter()
        candidates = search(
            query,
            client=client,
            top_k=retrieval_top_k,
            collection_name=COLLECTION_NAME,
        )
        search_time = (time.perf_counter() - search_started) * 1000

        if reranking_enabled:
            rerank_started = time.perf_counter()
            reranked = rerank(query, candidates, top_k=rerank_top_k)
            rerank_time = (time.perf_counter() - rerank_started) * 1000
            rerank_times.append(rerank_time)
        else:
            reranked = candidates[:rerank_top_k]

        search_times.append(search_time)
        pipeline_times.append((time.perf_counter() - started) * 1000)
        candidate_count = len(candidates)
        reranked_count = len(reranked)

    return QueryBenchmark(
        label=label,
        query=query,
        reranking_enabled=reranking_enabled,
        repeats=repeats,
        candidates=candidate_count,
        reranked_results=reranked_count,
        search_median_ms=statistics.median(search_times),
        search_p95_ms=percentile(search_times, 0.95),
        rerank_median_ms=(statistics.median(rerank_times) if rerank_times else None),
        rerank_p95_ms=(percentile(rerank_times, 0.95) if rerank_times else None),
        pipeline_median_ms=statistics.median(pipeline_times),
        pipeline_p95_ms=percentile(pipeline_times, 0.95),
    )


def print_report(results: list[QueryBenchmark]) -> None:
    print("ArchLens retrieval benchmark")
    print(f"Configuration: {results[0].label}")
    print(f"Queries: {len(results)}")
    print()
    print(
        f"{'Query':<54} {'Cand.':>5} {'Search med/p95':>18} "
        f"{'Rerank med/p95':>18} {'Pipeline med/p95':>20}"
    )
    print("-" * 122)

    for result in results:
        query_label = result.query[:51] + "..." if len(result.query) > 54 else result.query
        rerank_summary = (
            f"{result.rerank_median_ms:>7.1f}/{result.rerank_p95_ms:<7.1f}"
            if result.rerank_median_ms is not None
            else "       n/a/      n/a"
        )
        print(
            f"{query_label:<54} {result.candidates:>5} "
            f"{result.search_median_ms:>7.1f}/{result.search_p95_ms:<7.1f} "
            f"{rerank_summary} "
            f"{result.pipeline_median_ms:>8.1f}/{result.pipeline_p95_ms:<8.1f}"
        )

    all_pipeline_medians = [result.pipeline_median_ms for result in results]
    print()
    print(
        "Overall median of per-query pipeline medians: "
        f"{statistics.median(all_pipeline_medians):.1f} ms"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--warmup", type=int, default=1)
    parser.add_argument("--retrieval-top-k", type=int, default=10)
    parser.add_argument("--rerank-top-k", type=int, default=5)
    parser.add_argument(
        "--no-rerank",
        action="store_true",
        help="Run the semantic-search baseline without cross-encoder reranking.",
    )
    parser.add_argument(
        "--label",
        default=None,
        help="Name this benchmark configuration in the report and JSON output.",
    )
    parser.add_argument("--json", type=Path, help="Write detailed results to this JSON file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.repeats <= 0 or args.warmup < 0:
        raise ValueError("repeats must be positive and warmup cannot be negative.")
    if args.retrieval_top_k <= 0 or args.rerank_top_k <= 0:
        raise ValueError("top-k values must be positive.")

    client = get_qdrant_client()
    results = [
        benchmark_query(
            query,
            client=client,
            repeats=args.repeats,
            warmup=args.warmup,
            retrieval_top_k=args.retrieval_top_k,
            rerank_top_k=args.rerank_top_k,
            reranking_enabled=not args.no_rerank,
            label=args.label or ("search_only" if args.no_rerank else "search_plus_rerank"),
        )
        for query in DEFAULT_QUERIES
    ]

    print_report(results)

    if args.json:
        args.json.write_text(
            json.dumps([asdict(result) for result in results], indent=2),
            encoding="utf-8",
        )
        print(f"Detailed results written to {args.json}")


if __name__ == "__main__":
    main()
