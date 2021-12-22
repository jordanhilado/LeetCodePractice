# 443. String Compression
# https://leetcode.com/problems/string-compression/

def compress(self, chars: List[str]) -> int:
    slow = fast = 0 # set slow and fast pointers
    while fast < len(chars): # iterate through list
        chars[slow] = chars[fast] # set the character of the list
        ctr = 1 # set counter
        # while the next is the same
        while fast + 1 < len(chars) and chars[fast] == chars[fast + 1]:
            fast += 1 # increment fast and ctr
            ctr += 1
        # if ctr is greater than 1, then print the chars of the frequency
        if ctr > 1:
            for i in str(ctr):
                chars[slow + 1] = i
                slow += 1
        # increment slow and fast each iteration
        slow += 1
        fast += 1
    return slow