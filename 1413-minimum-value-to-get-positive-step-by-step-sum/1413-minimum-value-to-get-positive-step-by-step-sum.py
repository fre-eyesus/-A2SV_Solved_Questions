class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if nums[0] < 0:
            start = abs(nums[0]) + 1
        else:
            start = 1

        while True:
            arr = [start] + nums
            new = [arr[0]]
            check = True
            for i in range(1,len(arr)):
                sm = new[-1]+arr[i]
                if sm < 1:
                    check = False
                    break
                new.append(sm)
            if check:
                return start
            start += 1
            
            


            
