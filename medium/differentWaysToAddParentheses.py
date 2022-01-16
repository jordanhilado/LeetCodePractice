# 241. Different Ways to Add Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/

def diffWaysToCompute(self, expression: str) -> List[int]:
    nums = '0123456789'
    def op(a, b, c):
        if c == '+':
            return a + b
        elif c == '-':
            return a - b
        else:
            return a * b
    def func(l, r):
        if l == r:
            return [expression[l]]
        elif l > r:
            return []
        this = []
        went = 0
        for i in range(l, r + 1):
            if expression[i] not in nums:
                went = 1
                left = func(l, i - 1)
                right = func(i + 1, r)
                for leftVals in left:
                    for rightVals in right:
                        temp = op(int(leftVals), int(rightVals), expression[i])
                        print(temp)
                        this.append(temp)
        if went:
            return this
        else:
            return [expression[l:r + 1]]
    arr = func(0, len(expression) - 1)
    print(arr)
    return arr