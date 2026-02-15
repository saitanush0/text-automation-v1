import re

def generate_summary(text: str) -> str:
    """
    Offline summary (no API key):
    - strips noisy characters
    - keeps readable tokens
    - returns a short, clean digest
    """
    cleaned = text.strip()
    if not cleaned:
        return "No input text to summarize."

    # keep letters, numbers, spaces, and basic punctuation
    cleaned = re.sub(r"[^A-Za-z0-9\s.,!?'\-]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    if not cleaned:
        return "Text contains no readable content."

    # limit length to look like an actual summary
    return cleaned[:160] + "…" if len(cleaned) > 160 else cleaned
