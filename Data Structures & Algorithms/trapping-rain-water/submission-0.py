class Solution:
    def trap(self, height: List[int]) -> int:
        wawa = 0
        L, R = 0, len(height) - 1
        max_L, max_R = height[L], height[R]
        while L < R:
            if max_L <= max_R:
                L += 1
                max_L = max(max_L, height[L])
                # At here, we already know max_L < max_R, so we can safely calc the height
                # using max_L - height[L] without worrying about overflow on the right
                wawa += max_L - height[L]
            else:
                R -= 1
                max_R = max(max_R, height[R])
                # max_L is taller, so no overflow will happen on the left side
                wawa += max_R - height[R]
        return wawa