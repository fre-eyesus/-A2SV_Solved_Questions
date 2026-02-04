#User function Template for python3

class Solution:

    def isSubset(self, a, b):
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
    
    
        for num in b:
            if freq.get(num, 0) == 0:
                return False
            freq[num] -= 1
    
        return True
    
    
    
    
