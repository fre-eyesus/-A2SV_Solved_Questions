class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        count = 0

        for i in s:
            if counter_s[i] == counter_t[i]:
                count+= 1
        
        return count == len(t) and count == len(s)