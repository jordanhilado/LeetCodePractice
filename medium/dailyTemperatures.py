# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            curr = stack.pop()
            ans[curr] = i - curr
        stack.append(i)      
        print(stack, ans)
    return ans