class Solution:
     #calculates the sum of each digit square
    def sumOfSquares(self,n):
            total = 0

            while n > 0:
                digit = n % 10
                total +=  digit*digit 

                n //= 10
            return total
    def isHappy(self, n: int) -> bool:
      
        visited = set()

        while n > 1:
            if n in visited:
                return False
            visited.add(n)
            n = self.sumOfSquares(n)
        return True   
          
