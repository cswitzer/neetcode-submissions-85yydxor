class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a) - 1
        while True:
            """
            The idea is that we take i + 1 and j + 1 elements from the left and right
            arrays equaling half, or: 
            -> half = (i + 1) + (j + 1)
            -> half = i + j + 2
            -> j = half - i - 2
            """
            i = l + (r - l) // 2
            j = half - i - 2

            a_left = a[i] if i >= 0 else float("-infinity")
            a_right = a[i + 1] if i + 1 < len(a) else float("infinity")
            b_left = b[j] if j >= 0 else float("-infinity")
            b_right = b[j + 1] if j + 1 < len(b) else float ("infinity")

            # this means our pointers accurately reflect the left half of nums1 and nums2
            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                return min(a_right, b_right)
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1
