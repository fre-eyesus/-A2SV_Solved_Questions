class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key= lambda item: item[1])

        arrow = 1

        burst_end = points[0][1]

        for s, e in points:

            if s > burst_end:
                arrow+= 1
                burst_end = e
        
        return  arrow

        