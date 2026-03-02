class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        ans = []
        for i in range(len(nums)):
            total += sum(nums[0:i+1])
            ans.append(total)
            total = 0
        return ans