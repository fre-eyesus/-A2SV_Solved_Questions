class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        initial = strs[0]
        length = len(strs[0])

        for n in strs[1:]:
            while initial != n[0:length]:
                length -= 1

                if length == 0:
                    return ""
                
                initial = initial[0:length]

        return initial

        