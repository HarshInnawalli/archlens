# ArchLens

**Evidence-driven architecture analysis with agentic RAG**

> Don't ask whether an architecture is "good." Ask what claims it depends on, what evidence supports them, and what evidence challenges them.


<img width="800" height="450" alt="archlens_recording" src="https://github.com/user-attachments/assets/50c162ff-7880-4983-8b0b-f5896e81f054" />


## What it does

Most architecture reviews boil down to an LLM giving you its opinion. ArchLens breaks an architecture description into individual claims ("Redis Pub/Sub is suitable for reliable event processing"), then investigates each one against a technical knowledge base — actively searching for evidence that *supports* the claim and evidence that *challenges* it, rather than just confirming what you already believe.

```
Architecture → Claims + Requirements → Evidence Investigation → Claim Assessment → Report
```

Every verdict traces back to the actual evidence chunks that produced it.

## How it works

1. **Extract** claims and requirements from the architecture description
2. **Generate** a support query and a challenge query for each claim
3. **Retrieve** candidates from Qdrant, then rerank with a cross-encoder
4. **Check sufficiency** — is there enough evidence to actually judge this claim?
5. **Refine and retry** (up to 2 iterations) if evidence is thin
6. **Assess** the claim: `Supported`, `Partially Supported`, `Challenged`, or `Insufficient Evidence`
7. **Roll up** all claims into a final architecture report

A lack of evidence is treated as "insufficient evidence," not as evidence against a claim — those are different outcomes and ArchLens keeps them separate.

## Stack

LangGraph (orchestration) · Qdrant (vector store) · `bge-small-en-v1.5` (embeddings) · `bge-reranker-base` (reranking) · Streamlit (UI) · Ollama → Gemini → OpenRouter (LLM fallback chain, local-first)

## LangGraph Workflow & Optimization

ArchLens uses LangGraph to model architecture analysis as a stateful, iterative investigation rather than a single RAG call. Each claim is processed independently, while the graph maintains the architecture, extracted claims and requirements, retrieval results, evidence sufficiency, refinement state, and final assessments.

<img width="690" height="1122" alt="archlens-langgraph drawio" src="https://github.com/user-attachments/assets/cc4f54eb-f859-406c-8b05-301c92a5b468" />

The workflow is implemented through separate graph nodes for extraction, query generation, retrieval, evidence evaluation, refinement, assessment, and report generation. Conditional edges determine whether evidence refinement is necessary and whether the graph should continue processing claims.

**Retrieval & Reranking**
ArchLens uses a two-stage retrieval pipeline to improve evidence quality:

<img width="182" height="562" alt="archlens-retrieval-pipeline drawio" src="https://github.com/user-attachments/assets/0f8617a9-b670-4b75-b0d4-3be2966c82a6" />

**Semantic Retrieval**

Documents are embedded using BAAI/bge-small-en-v1.5 with 384-dimensional embeddings.

Qdrant performs the initial semantic retrieval and returns the top 10 candidate chunks.

**Cross-Encoder Reranking**

Rather than passing the raw vector-search results directly to the LLM, ArchLens applies BAAI/bge-reranker-base. The reranker evaluates each (query, evidence_chunk) pair and assigns a more fine-grained relevance score. 

The candidates are then sorted by reranking score and the top 8 evidence chunks are retained. This creates a deliberate separation between high-recall candidate retrieval, and
higher-precision evidence selection.

The reranking stage is particularly important for architecture analysis because semantically similar documents are not necessarily the most useful evidence for a specific technical claim.

**Bidirectional Evidence Retrieval**

For each claim, ArchLens generates two independent queries:

- Support Query: The support query searches for evidence consistent with the claim.
 
- Challenge Query: The challenge query searches for:

limitations
failure conditions
trade-offs
counterexamples
constraints
situations where the claim may not hold 

This is a deliberate design choice to avoid relying exclusively on confirmation-oriented retrieval.

## Benchmarking and Improvements

ArchLens includes a quantitative benchmark for the retrieval portion of the evidence-review pipeline. The benchmark measures semantic search, optional cross-encoder reranking, and the combined sequential retrieval pipeline across a fixed set of architecture questions.

### Running the benchmark

Prerequisites:

1. Start Qdrant on `http://localhost:6333`.
2. Build the `archlens` collection with the ingestion pipeline.
3. Activate the project virtual environment.

Run the default benchmark:

```powershell
py -m benchmark_retrieval
```

Run a more stable measurement with warm-up iterations and saved JSON output:

```powershell
py -m benchmark_retrieval --repeats 5 --warmup 1 --json benchmark.json
```

Measure semantic search without reranking:

```powershell
py -m benchmark_retrieval --no-rerank --label search_only
```

Compare a smaller candidate set before reranking:

```powershell
py -m benchmark_retrieval --retrieval-top-k 5 --rerank-top-k 5 --label top_k_5
```

The benchmark reports, for each query:

- Search median and p95 latency.
- Reranking median and p95 latency, when enabled.
- End-to-end retrieval pipeline median and p95 latency.
- Number of retrieved candidates and returned reranked results.

The p95 value is the interpolated 95th percentile over the measured repetitions. The benchmark reports retrieval latency only; it does not include LLM calls, claim extraction, query refinement, or final report generation.

### Current baseline

The checked-in benchmark results use eight representative architecture queries and five repetitions per query. They show a clear performance split:

| Configuration | Typical semantic search | Typical reranking | Main observation |
| --- | ---: | ---: | --- |
| Search only, 10 candidates | ~26-37 ms median | Not used | Qdrant retrieval is fast enough for interactive exploration. |
| Search plus reranking, 10 candidates | ~29-39 ms median | ~1.3-4.0 s median | Cross-encoder inference dominates the retrieval pipeline. |
| Search plus reranking, 5 candidates | ~28-46 ms median | ~1.3-1.8 s median | Reducing candidates materially lowers reranking cost, with a possible recall trade-off. |

These numbers are environment-dependent. They should be rerun after changing the embedding model, reranker model, hardware, corpus, chunking strategy, or Qdrant configuration. The JSON files in the repository are reference runs, not universal service-level objectives.

### Improvement priorities

#### 1. Keep the reranker warm

The reranker is loaded lazily through `get_reranker()`. Keep that model instance alive for the process lifetime and warm it up before serving user requests. This avoids turning the first query into a cold-start measurement and makes interactive latency more predictable.

#### 2. Reduce reranking work without losing recall

The current pipeline retrieves ten candidates and reranks up to eight in the graph workflow. Benchmark smaller candidate counts and compare them against a labeled relevance set before adopting a lower value. A two-stage strategy is a practical next step:

1. Use vector search to retrieve a modest candidate pool.
2. Rerank only the strongest candidates.

The goal is to reduce cross-encoder calls while preserving the evidence needed for both supporting and challenging searches.

#### 3. Add retrieval-quality metrics

Latency alone cannot show whether an improvement is useful. Add a small labeled evaluation set containing expected relevant documents or chunks for each query, then track:

- Recall@k: whether relevant evidence appears in the retrieved candidates.
- Precision@k: how much of the returned evidence is relevant.
- MRR or nDCG: whether the best evidence appears near the top.
- Support/challenge coverage: whether both sides of a claim receive useful evidence.

Record these metrics alongside latency in the benchmark JSON output.

#### 4. Compare reranker models and inference settings

Benchmark alternative cross-encoders, batch sizes, quantized variants, and CPU/GPU execution. Compare quality and latency together. A faster model is only an improvement if it does not remove the evidence needed for accurate claim assessments.

#### 5. Cache repeated work

Cache stable query embeddings and, where appropriate, retrieval results keyed by query, collection version, and model version. Include model and corpus identifiers in cache keys so stale evidence is not silently reused after reindexing.

#### 6. Measure the complete review path

Add a separate end-to-end benchmark around `build_graph().invoke(...)` or the streamed graph execution. Measure:

- Claim extraction latency.
- Retrieval and reranking latency per claim.
- Query-refinement frequency.
- Claim-assessment latency.
- Final report latency.
- Total review latency and token usage.

Keep this separate from the retrieval benchmark so infrastructure performance and LLM/provider performance remain distinguishable.

### Benchmarking discipline

For comparable runs, keep the following fixed and record them with every result:

- Query set and query order.
- Corpus version and document count.
- Chunking configuration.
- Embedding model and reranker model.
- Qdrant configuration.
- `retrieval-top-k`, `rerank-top-k`, repetitions, and warm-up count.
- CPU/GPU and Python environment details.

Run warm-up iterations, report both median and p95 latency, and compare quality metrics before treating a latency reduction as an overall improvement.
## Getting started

```bash
git clone https://github.com/HarshInnawalli/archlens.git
cd archlens
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env`:

```env
OLLAMA_MODEL=llama3.1:8b
OLLAMA_HOST=http://localhost:11434

GEMINI_MODEL=gemini-3.6-flash
GEMINI_API_KEY=your_gemini_key

OPENROUTER_MODEL=openrouter/free
OPENROUTER_API_KEY=your_openrouter_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

Start Qdrant:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Pull the local model:

```bash
ollama pull llama3.1:8b
```

Index your documents (dropped into `data/<topic>/`, supports `.md .txt .html .pdf`):

```bash
python -m app.ingestion.indexer
```

Run it:

```bash
streamlit run streamlit_app.py
```

Or test the graph directly without the UI:

```bash
python test_graph.py
```

## Example

Feed it something like:

> Clients connect through a REST API gateway. Internal services use gRPC. Redis stores sessions and distributes real-time updates via Pub/Sub. Kafka handles durable async events. PostgreSQL stores authoritative data. Must support 500,000 concurrent users with low latency.

ArchLens pulls out claims like "Redis Pub/Sub is suitable for distributing real-time updates" and "Kafka is suitable for durable event processing," separates out the hard requirements (500k users, low latency), and investigates each claim independently.

## Limitations (read this before trusting it)

- **Only as good as the corpus.** No relevant docs indexed → no reliable answer.
- **LLM-dependent** at every stage — extraction, query generation, assessment, all of it.
- **Retrieval can miss things.** Semantic search and reranking aren't perfect.
- **PDF extraction is imperfect**, especially for tables, diagrams, and multi-column layouts.
- **Capacity claims need real testing.** "Can this support 500k users?" isn't something literature retrieval can answer — that needs load testing against your actual implementation, hardware, and workload.

This is a research prototype meant to make reasoning more traceable, not a replacement for empirical validation.

## Roadmap

- Hybrid semantic + keyword retrieval, evidence deduplication, retrieval benchmarks
- Contradiction detection, claim dependency modeling, trade-off analysis
- Claim-to-evidence graph visualization, exportable reports, diagram ingestion
- A proper eval suite and a persistent, production-ready API layer

## License

MIT License

---
