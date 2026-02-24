class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)

        while right < len(haystack)+1:
            if haystack[left:right] == needle:
                return left
            left+= 1
            right = left + len(needle)

        return -1
        
        """if needle in haystack:
            return haystack.find(needle)
        else:
            return -1 """
