import os
import re

def _local_summary(text: str, max_sentences: int = 3) -> str:
    """
    Simple extractive summary: pick the first few meaningful sentences.
    Works offline, no API key needed.
    """
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return "No input text to summarize."

    # split into sentences (basic)
    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    sentences = [s for s in sentences if len(s.strip()) >= 20]  # skip tiny fragments

    if not sentences:
        # fallback: truncate
        return (cleaned[:200] + "…") if len(cleaned) > 200 else cleaned

    return " ".join(sentences[:max_sentences])

def generate_summary(text: str) -> str:
    """
    If OPENAI_API_KEY is present, you can later plug in an LLM call here.
    For now: always returns a strong offline summary (no cost).
    """
    # future-ready switch
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return _local_summary(text)

    # If you later add OpenAI SDK, replace this block with real API call.
    return _local_summary(text)
