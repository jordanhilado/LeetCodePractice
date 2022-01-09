# 824. Goat Latin
# https://leetcode.com/problems/goat-latin/

def toGoatLatin(self, sentence: str) -> str:
    s = sentence.split(" ")
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    a = 1
    ans = []
    for i in s:
        if i[0] in vowel:
            i += 'ma'
        elif i[0] not in vowel:
            i = list(i)
            first = i.pop(0)
            i.append(first)
            i = ''.join(i)
            i += 'ma'
        i += 'a' * a
        a += 1
        ans.append(i)
    return ' '.join(ans)