# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

#################### Reformatting Number Solution ####################

def hammingWeight(self, n: int) -> int:
    ans = 0
    num = '{:032b}'.format(n)
    for i in range(len(str(num))):
        if num[i] == "1":
            ans += 1
    return ans

#################### Using Counter ####################

def hammingWeight(self, n: int) -> int:
    counter = Counter(bin(n))
    return counter.get("1", 0)