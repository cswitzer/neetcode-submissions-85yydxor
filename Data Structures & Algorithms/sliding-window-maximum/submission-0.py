class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        left = 0
        for right in range(len(nums)):
            # Expand window to the right
            heapq.heappush(heap, (-nums[right], right))

            # Window size reached
            if right - left + 1 == k:
                # Remove expired elements (lazy deletion)
                while heap[0][1] < left:
                    heapq.heappop(heap)

                # Current max is at top of heap
                output.append(-heap[0][0])

                # Slide window
                left += 1

        return output
