class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()

        max_length = float('-inf')

        for i in range(1, len(nums)):
            max_length = max(nums[i]- nums[i - 1], max_length)
        return max_length
        

