from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            freqs[s[right]] += 1

            max_freq = max(freqs.values())

            leng = right - left + 1

            if leng - max_freq > k:
                freqs[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)


        return res