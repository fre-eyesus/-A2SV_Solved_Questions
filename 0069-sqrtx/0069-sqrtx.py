class Solution:
    def mySqrt(self, x: int) -> int:
        ans = -1
        low = 0
        high = x 

        while low <= high:
            mid = (low+high) //2
            if mid ** 2 == x:
                return mid
            elif mid** 2 > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans
        