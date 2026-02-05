class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums_new = [m for m in range(0,n +1)]

        missing_number = set(nums_new) - set(nums)
        missing = missing_number.pop()
        
        return missing 