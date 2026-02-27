class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zero_count, window, start= 0,0,0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            window  = max(window, right - start)

        return window