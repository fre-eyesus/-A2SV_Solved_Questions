class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.left(n)    

    def left(self,n):
        if n == 1:
            return 1
        
        return 2 * self.right(n // 2)
    def right(self,n):
        if n == 1:
            return 1
        if  n % 2:
            return 2 *self.left(n//2)
        else:
            return 2 * self.left(n//2) -1
    
