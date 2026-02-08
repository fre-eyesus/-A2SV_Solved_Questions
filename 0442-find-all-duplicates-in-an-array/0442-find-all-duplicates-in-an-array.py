class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        ans = []
        for key,value in counted.items():
            if value >=2:
                ans.append(key)
        return ans 