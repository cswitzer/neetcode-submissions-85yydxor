class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for ele_freq in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        for n, c in count.items():
            # indices represents the counts of each number in their lists
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result