# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/

def numberToWords(self, num: int) -> str:
    if num == 0:
        return 'Zero'
    ones = 'One Two Three Four Five Six Seven Eight Nine'.split()
    teens = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
    decs = 'Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    triples = 'Thousand Million Billion'.split()
    s, divs = [], 0
    while num:
        less1000 = num % 1000
        hundreds = less1000 // 100
        less100  = less1000 % 100
        tens = less100 // 10
        less10 = less100 % 10
        if divs and less1000: 
            s.append(triples[divs-1])
        if less100 in teens: 
            s.append(teens[less100])
        else:
            if less10: s.append(ones[less10-1])
            if tens: s.append(decs[tens-1])
        if hundreds:
            s.append('Hundred')
            s.append(ones[hundreds-1])
        num //= 1000
        divs += 1
    return ' '.join(s[::-1])