class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        merged.sort()

        n = len(merged)

        if  n % 2:
            return merged[n//2] 
        else:
            c = (n // 2)
            x = (n - 1) // 2
            ans = (merged[c] + merged[x])  / 2
            return ans
