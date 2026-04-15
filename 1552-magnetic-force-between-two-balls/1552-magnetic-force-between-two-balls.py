class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        head = 0
        tail = position[-1]

        def check(x):
            start = -1e100
            count = 0
            for p in position:
                if p - start >= x:
                    start = p
                    count += 1
            return count >= m
        
        while head <= tail:
            mid = ( head + tail ) // 2

            if check(mid+1):
                head = mid + 1
            else:
                tail = mid - 1
        return head