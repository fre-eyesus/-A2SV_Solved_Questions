from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        s_list = SortedList()

        ans = 0
        mod = 10**9 + 7
        for num in instructions:
            ans += min(s_list.bisect_left(num), len(s_list)- s_list.bisect_right(num))

            ans %= mod
            s_list.add(num)
        return ans