class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        if 0 < x:
            return False

        copy_x = x
        rev = 0
        while x > 0:
            rev = (rev * 10) + ( x % 10 ) 
            x //= 10
        if rev == copy_x:
            return True
        else:
            return False

