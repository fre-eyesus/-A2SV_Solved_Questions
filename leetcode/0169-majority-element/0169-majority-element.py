class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        majority = 0
        freq = 0
        for k, v in count.items():
            if v > freq:
                majority = k
                freq = v
        
        return majority 