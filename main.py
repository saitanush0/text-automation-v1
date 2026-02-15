from llm_utils import generate_summary
from datetime import datetime

def read_input():
    try:
        with open("input.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("❌ input.txt not found. Create the file and try again.")
        exit()

def process_text(text):
    upper_text = text.upper()
    word_count = len(text.split())
    char_count = len(text.replace(" ", "").replace("\n", ""))
    line_count = len(text.splitlines())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return upper_text, word_count, char_count, line_count, timestamp

def write_output(result):
    with open("output.txt", "w") as file:
        file.write(result)
    print("✅ Output saved to output.txt")

def main():
    input_text = read_input()
    summary = generate_summary(input_text)

    upper_text, word_count, char_count, line_count, timestamp = process_text(input_text)

    result = f"""
Original Text:
{input_text}

Uppercase Text:
{upper_text}

Word Count:
{word_count}

Character Count (no spaces):
{char_count}

Line Count:
{line_count}

Summary:
{summary}

Processed At:
{timestamp}
"""

    write_output(result)

if __name__ == "__main__":
    main()
