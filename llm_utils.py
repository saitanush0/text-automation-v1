import re

def generate_summary(text: str) -> str:
    """
    Offline extractive summary: picks the first 2 meaningful sentences.
    No API key required.
    """
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return "No input text to summarize."

    # Split sentences (basic)
    sentences = re.split(r"(?<=[.!?])\s+", cleaned)

    # Keep only meaningful ones (skip junk lines)
    sentences = [s.strip() for s in sentences if len(s.strip()) >= 25]

    if not sentences:
        # fallback: truncate
        return cleaned[:160] + "…" if len(cleaned) > 160 else cleaned

    return " ".join(sentences[:2])
