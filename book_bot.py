import argparse
import sys

# Version of the BookBot tool
__version__ = '1.0'

def get_book_text(path):
    """Reads and returns the content of a book file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        sys.exit(1)

def word_count(text):
    """Returns the total number of words in the text."""
    return len(text.split())

def chars_dict(text):
    """Creates a dictionary of character frequencies in the text."""
    stats = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            stats[char] = stats.get(char, 0) + 1
    return stats

def sort_chars(char_dict):
    """Sorts characters by frequency in descending order."""
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

def analyze_book(book_path):
    """Analyzes the book for word count and character frequency."""
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dictionary = chars_dict(text)
    sorted_chars = sort_chars(chars_dictionary)

    print(f"Number of words: {num_words}")
    for char, count in sorted_chars:
        print(f"Character: {char} - Count: {count}")

def main():
    parser = argparse.ArgumentParser(description="Analyze a text file for various statistics.")
    parser.add_argument('command', nargs='?', help="Command to execute (e.g., 'analyze')")
    parser.add_argument("--file", type=str, help="Path to the text file to be analyzed")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}", help="Show program's version number and exit.")

    args = parser.parse_args()

    if args.command == "analyze" and args.file:
        analyze_book(args.file)
    elif not args.command:
        parser.print_help()
    else:
        print("Invalid command or arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()
