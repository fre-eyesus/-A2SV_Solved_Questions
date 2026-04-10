class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        pos = defaultdict(list)
        
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = float('inf')
        
        for indices in pos.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    res = min(res, 2 * (indices[i+2] - indices[i]))
        
        return res if res != float('inf') else -1