# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:
    def __init__(self):
        self.data = {}
        self.real = []

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data[val] = len(self.real)
            self.real.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data[self.real[-1]], self.real[self.data[val]] = self.data[val], self.real[-1]
            self.real[-1] = val
            self.real.pop()
            self.data.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.real)