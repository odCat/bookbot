def count_words(text: str) -> int:
    return len(text.split())


def count_letters(text: str) -> dict[str, int]:
    result = {}
    for letter in text.lower():
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result


def sort_on(ch: tuple[str, int]) -> int:
    return ch[1]


def chars_dict_to_sorted_list(freq: dict[str, int]) -> list[tuple[str,int]]:
    result = [(key, freq[key]) for key in freq]
    return sorted(result, reverse=True, key=sort_on)
