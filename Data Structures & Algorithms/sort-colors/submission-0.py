class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for num in nums:
            buckets[num] += 1
        

        index = 0
        # [1, 2, 1] => one 0, two 1's, one 2
        for n in range(len(buckets)):
            for j in range(buckets[n]):
                nums[index] = n
                index += 1
