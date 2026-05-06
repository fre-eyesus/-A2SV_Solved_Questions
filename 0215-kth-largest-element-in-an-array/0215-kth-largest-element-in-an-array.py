class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = nlargest(k,nums)[-1]

        return k