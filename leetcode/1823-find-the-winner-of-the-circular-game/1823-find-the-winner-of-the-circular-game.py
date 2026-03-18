class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1,n+1))

        start = 0

        while len(circle) > 1:
            remove = (start + k -1) % len(circle)

            circle.pop(remove)

            start = remove
        
        return circle[0]