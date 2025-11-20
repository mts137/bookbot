import sys
from stats import get_word_count
from stats import get_character_counts
from stats import get_sorted_character_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    sorted_character_counts = get_sorted_character_counts(character_counts)

    character_count_report = ""
    for dict in sorted_character_counts:
        character = dict["char"]
        if not character.isalpha():
            continue
        count = dict["num"]
        character_count_report += f"{character}: {count}\n"
    if character_count_report:
        character_count_report = character_count_report[:-1]

    print(f"""\
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{character_count_report}
============= END ===============
""")

def get_book_text(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()
