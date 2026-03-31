class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [(idx, height)]
        max_area = 0
        

        for idx, height in enumerate(heights):
            # monotonic increasing stack
            starting_idx = idx
            while stack and height < stack[-1][1]:
                prev_idx, prev_height = stack.pop()
                prev_width = idx - prev_idx
                area = prev_height * prev_width
                max_area = max(max_area, area)
                
                # for extending backwards
                # e.g. [4, 5, 3], where 3 can extend backwards into 
                starting_idx = prev_idx
            
            stack.append((starting_idx, height))
        
        for idx, height in stack:
            width = len(heights) - idx
            area = height * width
            max_area = max(max_area, area)
        
        return max_area
        
