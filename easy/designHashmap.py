# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.data = [None] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        value = self.data[key]
        if value is not None:
            return value
        else:
            return -1

    def remove(self, key: int) -> None:
        self.data[key] = None