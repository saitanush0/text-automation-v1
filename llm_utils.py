import re

def generate_summary(text: str) -> str:
    """
    Offline extractive summary.
    Picks the first few meaningful sentences.
    Works without API keys.
    """
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return "No input text to summarize."

    # Split into sentences
    sentences = re.split(r"(?<=[.!?])\s+", cleaned)

    # Keep only meaningful ones
    sentences = [s for s in sentences if len(s.strip()) > 25]

    if not sentences:
        # fallback
        return cleaned[:200] + "…" if len(cleaned) > 200 else cleaned

    return " ".join(sentences[:2])
