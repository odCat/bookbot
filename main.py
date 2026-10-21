from stats import count_words, count_letters, chars_dict_to_sorted_list


def main():
    book_path = 'books/frankenstein.txt'
    content = get_content(book_path)
    word_count = count_words(content)
    print_report(book_path, word_count, count_letters(content))


def get_content(book_path):
    with open(book_path) as book:
        return book.read()


def print_report(book_file: str, word_count: int, letter_occur: dict[str, int]) -> None:
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_file}...')

    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')

    print("--------- Character Count -------")
    ordered = chars_dict_to_sorted_list(letter_occur)
    for key_value in ordered:
        if key_value[0].isalpha():
            print(f"{key_value[0]}: {key_value[1]}")

    print('\n--- End report ---')


main()