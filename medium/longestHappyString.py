# 1405. Longest Happy String
# https://leetcode.com/problems/longest-happy-string/

def longestDiverseString(self, a: int, b: int, c: int) -> str:
    s = [[a, 'a'], [b, 'b'], [c, 'c']]
    ans = []
    while True:
        # sort everytime, we will use the last one (-1) as the one to grab from
        s.sort()
        # grab from 1st index if the last two inserted characters are the same
        # and if the length of the word is greater than two
        # otherwise, grab from the last index
        i = 1 if len(ans) >= 2 and ans[-2] == ans[-1] == s[2][1] else 2
        if s[i][0]:
            ans.append(s[i][1])
            s[i][0] -= 1
        # if there are no remaining characters at current index, return answer
        else:
            break
    return ''.join(ans)