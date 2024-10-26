from collections import defaultdict
import sys


def count_words(book: str) -> int:
    return len(book.split())


def count_chars(book: str) -> dict[str, int]:
    chars = defaultdict(int)
    for ch in book:
        chars[ch.lower()] += 1
    return chars


def report(filename: str, words: int, chars: dict[str, int]) -> str:
    lines = [f"--- begin report of {filename} ---"]
    lines.append(f"{words} words found in the document")
    lines.append("")
    for ch, count in chars.items():
        if ch == "\n":
            ch = "\\n"
        lines.append(f"The '{ch}' character was found {count} times")
    return "\n".join(lines)


if __name__ == "__main__":
    if not sys.argv[1:]:
        raise RuntimeError("need file argument")
    filename = sys.argv[1]
    with open(filename) as file:
        book = file.read()

    words = count_words(book)
    chars = count_chars(book)
    print(report(filename, words, chars))
