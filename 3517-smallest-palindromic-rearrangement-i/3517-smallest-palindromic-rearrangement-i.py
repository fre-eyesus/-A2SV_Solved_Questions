class Solution:
    def smallestPalindrome(self, s: str) -> str:

        count = Counter(s)
        
        first = []
        middle = ''
        
        if len(s) == 1:
            return s

        for ch in sorted(count.keys()):
            if count[ch] % 2 != 0:
                middle = ch

            first.append(ch * (count[ch] // 2))
        m = list(middle)
        return ''.join(first + m + first[::-1])
        
