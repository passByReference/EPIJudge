"""
Datadog interview

第一题：地里高频的logs and queries match

设计一个queries search object，它每次读取一行信息string。当这个string格式是
"Q: hello world" 表示这是个queries， 内容是 hello world
如果string 格式是 “L: hello morning world”那么表示这是个log， 内容是 hello morning world。 每次读取query要保存query内容并赋予query id， 每次读取log要把所有在这个log中出现的query id给出来。 这里出现的定义是如果query的每一个word都在log中出现了。注意这里有可能要求log中相同word的出现次数要多于或等于在query中出现的次数，也可能不要求次数，word只要出现即可。但不管怎样，在log中的每个word都能和不同的query中的word重复而独立的匹配。解法是用地里之前提到的reverted index 去记录每一个word在哪些query中出现了，然后遇到log把每个word带入reverted index 去重建 qid-> words list 结构然后和那个qid的word list相比较。

"""

class LogAndQuery:
    def __init__(self):
        self.queries = {}
        self.invertedIndex = defaultdict(list)
        self.query_id = 1

    def get_hash(self, words):
        words.sort()
        return "_".join(words)

    def input(self, entry:str):
        label, text = entry.split(":")
        words = text.split()
        query_hash = self.get_hash(words)
        if label == "Q":
            if query_hash not in self.queries:
                self.queries[query_hash] = self.query_id
                for word in words:
                    self.invertedIndex[word].append(self.query_id)
                self.query_id += 1
            print()
        else:
            result = []
            candidate_queries = defaultdict(list)
            for word in words:
                for q_id in self.invertedIndex[word]:
                    candidate_queries[q_id].append(word)
            for cq, words in candidate_queries.items():
                word_hash = self.get_hash(words)
                if word_hash in self.queries:
                    result.append(cq)
            print()

            