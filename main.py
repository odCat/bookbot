def count_letters(text):
    result = {}
    for letter in text.lower():
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result


with open('books/frankenstein.txt') as book:
    content = book.read()
    print(count_letters(content))
    words = content.split()
    print(len(words))
