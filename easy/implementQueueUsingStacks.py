# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop(0)

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        if len(self.data) == 0:
            return True
        else:
            return False