# 398. Random Pick Index
# https://leetcode.com/problems/random-pick-index/

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        answer = []
        for i, num in enumerate(self.nums):
            print(i, num)
            if target == num:
                answer.append(i)
        return random.choice(answer)