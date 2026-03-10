class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, hot = stack.pop()
                ans[index] = (idx - index)
            stack.append([idx,temp])
        return ans

