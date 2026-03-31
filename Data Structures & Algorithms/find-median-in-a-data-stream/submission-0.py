class MedianFinder:
    """
    The idea is this. We keep track of two heaps. The max heap represents the greatest elements
    in the LOWER half of the numbers, while the min heap represents the min elements of the
    UPPER half of the numbers. This means that the max and min heap at index 0 is guaranteed
    to be a value that can help us find the median

    Every single time we add a number to the median finder, we - 

    1. Check if it is larger than the min number on the left side. If so, add it to min
    2. If not, add it to the max
    3. Because we want to find the median, the different in the # of elements between the heaps cannot > 1
    4. If an imbalance occurs, move the top of the smaller heap to the bigger
    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # if the number is larger than the min
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        min_len = len(self.min_heap)
        max_len = len(self.max_heap)
        diff = abs(max_len - min_len)
        if max_len < min_len and diff > 1:
            min_el = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_el)
        if min_len < max_len and diff > 1:
            max_el = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -max_el)

    def findMedian(self) -> float:
        if self.min_heap and not self.max_heap:
            return self.min_heap[0]
        if self.max_heap and not self.min_heap:
            return -self.max_heap[0]

        even_len = len(self.max_heap) == len(self.min_heap) 
        if even_len:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]

        