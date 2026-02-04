class Solution:    
    def findUnion(self, a, b):
        # code here
        union = a + b
        union.sort()
        dst = set(union)
        
        
        return dst
