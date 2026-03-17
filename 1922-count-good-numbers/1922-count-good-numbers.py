class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(x, y):
            if y == 0:
                return 1

            if y % 2 == 0:
                half = power(x, y // 2)
                return (half * half) % MOD
            else:
                return (x * power(x, y - 1)) % MOD

        even = (n + 1) // 2
        odd = n // 2

        return (power(5, even) * power(4, odd)) % MOD