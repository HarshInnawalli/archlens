import json
import re
from typing import Type

from pydantic import BaseModel
from app.llm.providers import invoke_with_fallback


class ArchitectureClaim(BaseModel):
    claim: str
    category: str
    importance: str


class ArchitectureRequirement(BaseModel):
    requirement: str
    category: str
    importance: str


class ClaimExtractionResult(BaseModel):
    claims: list[ArchitectureClaim] = []
    requirements: list[ArchitectureRequirement] = []


class SearchQuery(BaseModel):
    query: str


class RefinedQueries(BaseModel):
    support_query: str
    challenge_query: str


class EvidenceSufficiency(BaseModel):
    sufficient: bool
    reasoning: str
    missing_aspects: list[str] = []


class ClaimAssessment(BaseModel):
    claim: str
    verdict: str
    reasoning: str
    supporting_evidence_ids: list[str] = []
    challenging_evidence_ids: list[str] = []
    missing_information: list[str] = []


def _extract_json(text: str) -> str:
    """
    Extract a JSON object from an LLM response.
    Handles Markdown code fences and empty/non-string responses.
    """

    if not text:
        raise ValueError("LLM returned an empty response.")

    text = str(text).strip()

    # Remove ```json ... ``` if present
    text = re.sub(
        r"```(?:json)?\s*(.*?)\s*```",
        r"\1",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    ).strip()

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1 or end <= start:
        raise ValueError(
            f"No JSON object found in LLM response.\n"
            f"Raw response: {text!r}"
        )

    return text[start:end + 1]


def invoke_structured(
    llm,
    prompt: str,
    schema: Type[BaseModel],
):
    """
    Ask the LLM for JSON and validate the result with Pydantic.
    """

    response = invoke_with_fallback(prompt)

    raw = response.content

    print("\n===== RAW LLM RESPONSE =====")
    print(repr(raw))
    print("===== END RAW RESPONSE =====\n")

    json_text = _extract_json(raw)

    try:
        data = json.loads(json_text)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"LLM returned invalid JSON:\n{json_text}"
        ) from e

    return schema.model_validate(data)

def structured_llm(llm, schema):
    """
    Backward-compatible wrapper.

    Existing nodes may still import this function.
    """
    from langchain_core.runnables import RunnableLambda

    def invoke(input_data):
        return invoke_structured(
            llm=llm,
            prompt=input_data,
            schema=schema,
        )

    return RunnableLambda(invoke)