class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[right], height[left])
            result = max(result, area)

            if height[left] < height[right]:
                left += 1  # Move left pointer forward
            else:
                right -= 1  # Move right pointer backward

        return result  