import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash",
)

OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openrouter/free",
)

OPENROUTER_BASE_URL = os.getenv(
    "OPENROUTER_BASE_URL",
    "https://openrouter.ai/api/v1",
)

# ---------------------------------------------------------
# Individual providers
# ---------------------------------------------------------

@lru_cache(maxsize=1)
def get_ollama_llm():
    from langchain_ollama import ChatOllama

    return ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_HOST,
        temperature=0,
    )


@lru_cache(maxsize=1)
def get_gemini_llm():
    from langchain_google_genai import ChatGoogleGenerativeAI

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set."
        )

    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=api_key,
        temperature=0,
    )


@lru_cache(maxsize=1)
def get_openrouter_llm():
    from langchain_openai import ChatOpenAI

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set."
        )

    return ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=api_key,
        base_url=OPENROUTER_BASE_URL,
        temperature=0,
        default_headers={
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "ArchLens",
        },
    )


# ---------------------------------------------------------
# Provider list
# ---------------------------------------------------------

@lru_cache(maxsize=1)
def get_llm_providers():
    """
    Returns providers in failover order.

    Ollama -> Gemini -> OpenRouter
    """

    providers = []

    # Ollama is always attempted first.
    try:
        providers.append(
            ("ollama", get_ollama_llm())
        )
    except Exception as e:
        print(f"[LLM] Ollama unavailable: {e}")

    # Gemini is second.
    try:
        providers.append(
            ("gemini", get_gemini_llm())
        )
    except Exception as e:
        print(f"[LLM] Gemini unavailable: {e}")

    # OpenRouter is final fallback.
    try:
        providers.append(
            ("openrouter", get_openrouter_llm())
        )
    except Exception as e:
        print(f"[LLM] OpenRouter unavailable: {e}")

    if not providers:
        raise RuntimeError(
            "No LLM providers are configured."
        )

    return providers


def get_llm():
    """
    Backwards-compatible helper.

    Returns the first configured provider.
    """

    return get_llm_providers()[0][1]

def invoke_with_fallback(prompt: str):
    errors = []

    for provider_name, llm in get_llm_providers():
        try:
            print(f"\n[LLM] Trying provider: {provider_name}")
            response = llm.invoke(prompt)
            print(f"[LLM] Success: {provider_name}")
            return response

        except Exception as e:
            print(f"[LLM] Failed: {provider_name} -> {e}")
            errors.append(f"{provider_name}: {e}")

    raise RuntimeError(
        "All LLM providers failed:\n" + "\n".join(errors)
    )