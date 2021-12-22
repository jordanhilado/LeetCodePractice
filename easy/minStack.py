# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = float("inf")
        self.prevMins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.currMin:
            self.prevMins.append(self.currMin)
            self.currMin = val

    def pop(self) -> None:
        if self.stack[-1] == self.currMin:
            self.currMin = self.prevMins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin