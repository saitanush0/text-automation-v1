def generate_summary(text):
    text = " ".join(text.split())
    if not text:
        return "No input text to summarize."
    return (text[:200] + "…") if len(text) > 200 else text
