class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)

        if max(count.values()) == 1:
            return 0
        
        counter = 0
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i] ==  nums[j] and i * j % k == 0 and i < j:
                    counter+= 1
        return counter 