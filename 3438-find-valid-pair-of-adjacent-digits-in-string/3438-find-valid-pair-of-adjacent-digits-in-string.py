class Solution:
    def findValidPair(self, s: str) -> str:

        count = Counter(s)

        for i in range(len(s)-1):
            valid = s[i:i+2]
            num = list(map(int,list(valid)))

            if num[0] != num[1] and count[str(num[0])] == num[0] and count[str(num[1])] == num[1]:
                return valid
        return ""
