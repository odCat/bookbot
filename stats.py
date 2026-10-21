def count_words(text: str) -> int:
    return len(text.split())


def count_letters(text: str) -> dict[str, int]:
    result = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
    return result


