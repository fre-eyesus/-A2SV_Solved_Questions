class Solution:
    def mirrorDistance(self, n: int) -> int:
        # s = list(str(n))
        # rev = s[::-1]
        # rev_num = int(''.join(rev))

        # ans = abs(n - rev_num)
        # return ans

        def reverse(x):
            res = 0

            while x > 0:
                res = res * 10 + x % 10
                x //= 10
            return res                
        return abs(n - reverse(n))

