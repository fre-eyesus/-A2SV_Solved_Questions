class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for n in nums1:
            vl = -1
            found = False

            for n2 in nums2:
                if  n == n2:
                    found = True
                if found:
                    if n2 > n:
                        vl = n2
                        break
            ans.append(vl)
        return ans