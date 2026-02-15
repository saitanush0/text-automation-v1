import argparse
from llm_utils import generate_summary
from datetime import datetime


def read_input(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ {filepath} not found.")
        exit()


def process_text(text):
    upper_text = text.upper()
    word_count = len(text.split())
    char_count = len(text.replace(" ", "").replace("\n", ""))
    line_count = len(text.splitlines())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return upper_text, word_count, char_count, line_count, timestamp


def write_output(result, filepath):
    with open(filepath, "w") as file:
        file.write(result)
    print(f"✅ Output saved to {filepath}")


def main():
    parser = argparse.ArgumentParser(
        prog="ta-cli",
        description="Text Automation Tool (offline NLP summary + text stats)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Example:\n  python main.py --input input.txt --output output.txt --summarize"
)

    parser.add_argument(
    "--input", "--in",
    dest="input_file",
    default="input.txt",
    help="Path to input text file"
)
    parser.add_argument(
    "--output", "--out",
    dest="output_file",
    default="output.txt",
    help="Path to output file"
)
    parser.add_argument(
    "--summarize",
    action="store_true",
    help="Add offline NLP summary section"
)


    args = parser.parse_args()

    input_text = read_input(args.input_file)

    upper_text, word_count, char_count, line_count, timestamp = process_text(input_text)

    summary = generate_summary(input_text) if args.summarize else "Summary disabled."

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

Summary (offline NLP):
{summary}

Processed At:
{timestamp}
"""

    write_output(result, args.output_file)


if __name__ == "__main__":
    main()
