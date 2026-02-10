class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            n = list(map(int,list(str(nums[i]))))
            ans.extend(n)

        return ans
