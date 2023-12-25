def main():
    book_path = 'books/frankenstein.txt'
    content = get_content(book_path)
    word_count = count_words(content)
    print_report(book_path, word_count, count_letters(content))


def get_content(book_path):
    with open(book_path) as book:
        return book.read()

def count_words(text):
    return len(text.split())


def count_letters(text):
    result = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
    return result


def print_report(book_file, word_count, letter_occur):
    print(f'--- Begin report of {book_file} ---')
    print(f'{word_count} words found in the documment\n')

    ordered = [x for x in letter_occur.values()]
    ordered.sort(reverse=True)
    for occur in ordered:
        for letter in letter_occur:
            if letter_occur[letter] == occur:
                print(f"The '{letter}' character was found {letter_occur[letter]} times")
    
    print('\n--- End report ---')


main()