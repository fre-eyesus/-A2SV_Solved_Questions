class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if num % 3  == 0:
            n1= int(num / 3)
            ans.extend([n1- 1,n1,n1+1])
        return ans