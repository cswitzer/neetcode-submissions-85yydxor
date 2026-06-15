class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Calculate counts for each number
        2. Init list, where each index is a list
        3. Each index represents the count of all elements in its list
        4. While the result length is < k, keep adding from (i - 1) to 0
        """
        # Step 2 complete
        counts = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 1 complete
        for num in nums:
            counts[num] += 1
        
        # Step 3 complete
        for number, count in counts.items():
            freq[count].append(number)
        
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
            