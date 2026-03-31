class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # right - left is width, smallest beam is height
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, width * height)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area