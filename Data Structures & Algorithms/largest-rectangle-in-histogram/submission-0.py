class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (idx, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i # don't know if we can extends backwards yet
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # We just popped a rectangle higher than the current, so we can extend backwards
                # via setting the start to the index of the popped element
                start = index
            stack.append((start, h))
        
        # the entries that extend all the way to the end of the histogram
        # we must compute these areas too to discover a possible max area
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
        