from typing import Set
import string

from test_framework import generic_test
from collections import deque, namedtuple

def transform_string(D: Set[str], s: str, t: str) -> int:
    # TODO - you fill in here.
    if s not in D or t not in D:
        return -1

    StringWithDistance = namedtuple("StringWithDistance", ("candadate_string", "distance"))
    to_visit = deque([StringWithDistance(s, 0)])
    D.remove(s)
    while to_visit:
        curr = to_visit.popleft()
        if curr.candadate_string == t:
            return curr.distance
        for i in range(len(curr.candadate_string)):
            for c in string.ascii_lowercase:
                next_word = curr.candadate_string[:i] + c + curr.candadate_string[i+1:] # slicing doesn't throw error with out-of-range slice
                if next_word in D:
                    D.remove(next_word)
                    to_visit.append(StringWithDistance(next_word, curr.distance + 1))
        
    return -1

    """
    if s not in D or t not in D:
        return -1
    g = {}
    for w in D:
        if w not in g:
            g[w] = []
        for new_word in D:
            if new_word != w and len(new_word) == len(w):
                count = 0
                for i in range(len(w)):
                    if w[i] == new_word[i]:
                        count += 1
                if count == len(w) - 1:
                    g[w].append(new_word)
    

    to_visit = deque()
    to_visit.append(s)
    visited = set()
    visited.add(s)
    path = 0
    while to_visit:
        curr = to_visit.popleft()
        if curr == t:
            return path
        for neighbor in g[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                to_visit.append(neighbor)
                path += 1 # this records all the paths tried before reaching t, not the shortest path

    
    return 0
   """






































    """
    if s not in D or t not in D:
        return -1
    StringWithDistance = namedtuple("StringWithDistance", ("candidate_string", "distance"))
    q = deque([StringWithDistance(s, 0)])
    D.remove(s)
    while len(q) > 0:
        curr = q.popleft()
        if curr.candidate_string == t:
            return curr.distance
        for i in range(len(curr.candidate_string)):
            for c in string.ascii_lowercase:
                candidate = curr.candidate_string[:i] + c + curr.candidate_string[i+1:]
                if candidate in D:
                    D.remove(candidate)
                    q.append(StringWithDistance(candidate, curr.distance + 1))
    return -1

    '''
    # Construct a graph where node is connected to another via exactly 1 different letter
    g = {}
    for w in D:
        if w not in g:
            g[w] = []
        for n_word in D:
            if len(n_word) == len(w):
                i = 0
                count = 0
                while i < len(w):
                    if n_word[i] == w[i]:
                        count += 1
                    i += 1
                if count == len(w) - 1:
                    g[w].append(n_word)
    # BFS the graph
    to_visit = deque()
    to_visit.append(s)
    visited = set()
    visited.add(s)
    path = 0
    while len(to_visit) > 0:
        curr = to_visit.popleft()
        if curr == t:
            return path
        for node in g[curr]:
            if node not in visited:
                visited.add(node)
                to_visit.append(node)
                path += 1
        


        
    return 0
    '''

"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
