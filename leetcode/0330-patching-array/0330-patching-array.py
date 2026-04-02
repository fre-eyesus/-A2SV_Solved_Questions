class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, ans , reach = 0, 0, 0

        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                reach += nums[i]
                i += 1
            else:
                reach += (reach + 1)
                ans += 1
        return ans

