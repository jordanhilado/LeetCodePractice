# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.data[len(word)].append(word)

    def search(self, word: str) -> bool:
        words = self.data[len(word)]
        for index, char in enumerate(word):
            words = [w for w in words if char in ('.', w[index])]
            if not words:
                return False
        return True