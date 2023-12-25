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


def main():
    with open('books/frankenstein.txt') as book:
        content = book.read()
        words = content.split()
        # letters = list(count_letters(content)).sort()
        print_report('books/frankenstein.txt', len(words), count_letters(content))


main()