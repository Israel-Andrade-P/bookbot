import stats
import sys

def get_book_text(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()
    
def main():
    if len(sys.argv) <= 1:
        print("Usage: py/python/python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = stats.get_word_count(file_contents)
    character_count = stats.get_character_count(file_contents)
    sorted_chars = stats.get_sorted_list(character_count)

    print(f"\n============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n")
    print(f"----------- Word Count ----------\nFound {word_count} total words\n")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}:{char_dict["num"]}\n")
    print("============= END ===============")

main()        