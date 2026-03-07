class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        ans = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            md = cur_sum % k
            ans += count.get(md,0)

            count[md] = 1 + count.get(md,0)
        return ans
