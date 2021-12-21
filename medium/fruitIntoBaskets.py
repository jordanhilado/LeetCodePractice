# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/

def totalFruit(self, fruits: List[int]) -> int:
    types = Counter()
    diff = maxCnt = left = right = 0
    while right < len(fruits):
        if types[fruits[right]] == 0:
            diff += 1
        types[fruits[right]] += 1
        while diff > 2:
            types[fruits[left]] -= 1
            if types[fruits[left]] == 0:
                diff -= 1
            left += 1
        maxCnt = max(maxCnt, right - left + 1)
        right += 1
    return maxCnt