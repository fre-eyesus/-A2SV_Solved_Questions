class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = []
        count = 0
        left = 0
        right = n-1
        while left < n:
            while right >= 0:

                if left != right and nums[left] > nums[right]:
                    count+= 1
                
                right-= 1
            left += 1
            right = n - 1
            ans.append(count)
            count = 0
        return ans