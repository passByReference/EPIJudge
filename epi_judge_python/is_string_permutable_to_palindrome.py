from test_framework import generic_test

from collections import Counter
def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    word_map = Counter(s)
    odd_count = 0
    for v in word_map.values():
        if v % 2 != 0:
            odd_count += 1
    
    if len(s) % 2 == 0:
        return odd_count == 0
    else:
        return odd_count == 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
