from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # TODO - you fill in here.
    word_map = {}
    shortest_distance = -1
    for idx, w in enumerate(paragraph):
        if w not in word_map:
            word_map[w] = idx
        else:
            shortest_distance = idx - word_map[w] if shortest_distance == -1 else min(shortest_distance, idx - word_map[w])
            word_map[w] = idx
              

    return shortest_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
