class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left,right =0,floor(sqrt(c))

        while left <= right:
            squared = left ** 2 + right ** 2
            if squared == c:
                return True
            
            if c > squared:
                left += 1
            else:
                right -= 1
        
        return False
            