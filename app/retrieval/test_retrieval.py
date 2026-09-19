from app.retrieval.search import search, print_results
from app.retrieval.reranker import rerank


query = "Is Redis Pub/Sub suitable for reliable event processing?"

results = search(
    query=query,
    top_k=10,
)

print("\n\n===== SEMANTIC SEARCH =====")
print_results(results)

reranked = rerank(
    query=query,
    results=results,
    top_k=5,
)

print("\n\n===== RERANKED RESULTS =====")

for i, result in enumerate(reranked, 1):
    print(f"\nRESULT {i}")
    print(f"Semantic Score: {result.score:.4f}")
    print(f"Rerank Score:   {result.rerank_score:.4f}")