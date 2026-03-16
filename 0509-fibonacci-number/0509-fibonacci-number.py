class Solution:
    def fib(self, n: int) -> int:
        # best case, if n is less than 1
        if n <= 1:
            return n
        
        prefix = [0] * (n + 1)
        prefix[1] = 1
        
        for i in range(2, n + 1):
            prefix[i] = prefix[i-1] + prefix[i-2]
        
        return prefix[n]