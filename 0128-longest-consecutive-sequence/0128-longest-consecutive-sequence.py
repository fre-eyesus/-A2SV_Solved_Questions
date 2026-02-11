class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = list(set(nums))
        unique.sort()
        
        if len(nums) == 0:
            return 0
        count = 0
        ans = 0
        for i in range(len(unique)-1):
            if unique[i+1] - unique[i] == 1:
                count+= 1
            else:
                count = 0
            ans = max(ans, count)
        return ans + 1