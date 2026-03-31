class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range(n + 1):
            curr_num = i
            count = 0
            for _ in range(32):
                if curr_num & 1 == 1:
                    count += 1
                curr_num >>= 1
            counts.append(count)
        return counts