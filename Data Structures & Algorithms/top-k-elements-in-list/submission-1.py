class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # indices represent number of times element appears
        # e.g. 0 -> 3 times, 1 -> 1 time, 5 -> 8 times
        count = {}
        freq = [[] for ele_freq in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            # n occurs c number of times
            # e.g. 1 and 2 show 4 times or 4 -> [1, 2]
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # for each element in the sublist
                res.append(n)
                if len(res) == k:
                    return res