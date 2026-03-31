class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for right, val in enumerate(nums):
            heapq.heappush(heap, (-val, right))
            
            # Once the window is full
            if right >= k - 1:
                # Remove top element if it's out of bounds
                while heap[0][1] < right - k + 1:
                    heapq.heappop(heap)
                    
                output.append(-heap[0][0])

        return output
