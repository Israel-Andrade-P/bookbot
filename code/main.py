from stats import get_word_count, get_character_count

def get_book_text(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()
    
def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)

    print(f"{word_count} words found in the document")
    print(character_count)

main()        