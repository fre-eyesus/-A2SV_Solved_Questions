class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0:1}
        total, ans= 0,0

        for r in range(len(nums)):
            total += nums[r]

            ans += count.get(total- goal,0)

            count[total] = 1 + count.get(total,0)
          
        return ans 