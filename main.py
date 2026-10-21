from stats import count_words, count_letters


def main():
    book_path = 'books/frankenstein.txt'
    content = get_content(book_path)
    word_count = count_words(content)
    print_report(book_path, word_count, count_letters(content))


def get_content(book_path):
    with open(book_path) as book:
        return book.read()


def print_report(book_file, word_count, letter_occur):
    print(f'--- Begin report of {book_file} ---')
    print(f'Found {word_count} total words\n')

    ordered = [x for x in letter_occur.values()]
    ordered.sort(reverse=True)
    for occur in ordered:
        for letter in letter_occur:
            if letter_occur[letter] == occur:
                print(f"The '{letter}' character was found {letter_occur[letter]} times")
    
    print('\n--- End report ---')


main()