class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appear = floor(len(nums) / 3) 
        counted = Counter(nums)

        ans = []

        for k,v in counted.items():
            if v > appear:
                ans.append(k)
        return ans

