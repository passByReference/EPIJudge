from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # TODO - you fill in here.
    letter_count_map = {}
    for w in letter_text:
        if w not in letter_count_map:
            letter_count_map[w] = 0
        letter_count_map[w] += 1
    
    for w in magazine_text:
        if w in letter_count_map:
            letter_count_map[w] -= 1
            if letter_count_map[w] == 0:
                del letter_count_map[w]
                if not letter_count_map:
                    return True
           
    return len(letter_count_map) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
