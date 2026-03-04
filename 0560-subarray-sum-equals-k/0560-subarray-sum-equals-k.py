class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix = {0: 1}

        for i in range(len(nums)):
            cur_sum += nums[i]

            dif = cur_sum - k
            res += prefix.get(dif, 0)

            prefix [cur_sum] = 1 + prefix.get(cur_sum, 0)
        return res 