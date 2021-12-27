# 384. Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.data[:] = self.original
        return self.data

    def shuffle(self) -> List[int]:
        random.shuffle(self.data)
        return self.data