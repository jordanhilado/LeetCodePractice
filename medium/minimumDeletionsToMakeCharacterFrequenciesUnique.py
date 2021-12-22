# 1647. Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

def minDeletions(self, s: str) -> int:
    c = Counter(s)
    unique = set()
    count = 0
    for char, freq in c.items():
        while freq > 0 and freq in unique:
            freq -= 1
            count += 1
        unique.add(freq)
    return count