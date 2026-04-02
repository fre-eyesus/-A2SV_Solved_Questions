class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check (capacity, weights):
            day = 1
            cur_sum = 0
            for w in weights:
                if w + cur_sum > capacity:
                    day += 1
                    cur_sum = w
                else:
                    cur_sum += w
            
            return day <= days
        
        ans = -1
        left = max(weights)
        right= sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if check(mid, weights):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


                