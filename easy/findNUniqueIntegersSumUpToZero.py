# 1304. Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

def sumZero(self, n: int) -> List[int]:
    l, half, ctr = [0] * n, n // 2, 0
    for i in range(len(l)):
        if ctr == 2:
            half -= 1
            ctr = 0
        half = -half
        l[i] += half
        ctr += 1
    return l