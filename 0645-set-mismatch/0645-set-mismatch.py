class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        original = range(1, len(nums)+1)
        ans = []
        count = Counter(nums)
        
        ans.extend([k for k,f in count.items() if f == 2])

        ans.extend(set(original)- set(nums))

        
        return ans