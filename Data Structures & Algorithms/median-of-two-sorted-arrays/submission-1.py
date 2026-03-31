class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total  // 2

        if len(b) < len(a):
            a, b = b, a
        
        # left and right pointers for the smaller array
        l, r = 0, len(a) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            a_left = a[i] if i >= 0 else float("-inf")
            b_left = b[j] if j >= 0 else float("-inf")
            a_right = a[i + 1] if (i + 1) < len(a) else float("inf")
            b_right = b[j + 1] if (j + 1) < len(b) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2 != 0:
                    # When total is odd, the left partition has `half` elements
                    # and the median is the first element in the right partition,
                    # which is min(a_right, b_right)
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            
            # We took too little elements from array "a". We need to take more
            elif b_left > a_right:
                l = i + 1
            
            # we took too little elements from array "b". Take more
            else:
                r = i - 1
