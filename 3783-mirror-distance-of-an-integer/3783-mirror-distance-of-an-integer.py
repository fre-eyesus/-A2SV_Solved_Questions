class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = list(str(n))
        rev = s[::-1]
        rev_num = int(''.join(rev))

        ans = abs(n - rev_num)
        return ans