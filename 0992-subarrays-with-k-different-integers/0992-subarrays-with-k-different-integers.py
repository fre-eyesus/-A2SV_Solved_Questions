class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        count=0
        
        l_near,l_far,right = 0  , 0, 0
        
        dis = defaultdict(int)

        for r in range(len(nums)):
            dis[nums[r]] += 1

            while len(dis) > k:
                dis[nums[l_near]] -= 1

                if dis[nums[l_near]] == 0:
                    dis.pop(nums[l_near])

                l_near += 1
                l_far = l_near
            while dis[nums[l_near]] > 1:
                dis[nums[l_near]] -= 1
                l_near += 1
            
            if len(dis) == k:
                count += l_near - l_far + 1
            
    
        
        return count




        