from math import ceil

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0

        prev = nums[-1]

        for i in range(n - 2 , -1 , -1):
            num = nums[i]

            k = ceil(num / prev)

            ops += k - 1
            prev = num // k
            
        return ops
        