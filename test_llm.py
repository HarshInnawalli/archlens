from app.llm.providers import get_llm
from app.llm.structured import ClaimExtractionResult, structured_llm

llm = get_llm()

structured = structured_llm(llm, ClaimExtractionResult)

architecture = """
I’m building a real-time collaborative document application.
Frontend → REST API gateway → three synchronous backend services.
PostgreSQL stores documents.
Redis stores sessions and Pub/Sub.
Expect 100k concurrent users.
Prioritize low latency over consistency.
"""

result = structured.invoke(
    f"""
Extract architecture claims and requirements from this architecture description.

Architecture:
{architecture}
"""
)

print("RAW RESULT:")
print(result)

print("\nCLAIMS:")
for claim in result.claims:
    print("-", claim.claim)

print("\nREQUIREMENTS:")
for req in result.requirements:
    print("-", req.requirement)