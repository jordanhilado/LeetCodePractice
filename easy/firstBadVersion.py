# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    l, r = 1, n
    while l <= r:
        m = l + (r - l) // 2
        if isBadVersion(m) == False:
            l = m + 1
        else:
            r = m - 1
    return l