class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = deque() # tuples of (prev_idx, prev_temp)

        for idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][1]:
                prev_idx, prev_temp = stack.pop()
                result[prev_idx] = idx - prev_idx
            stack.append((idx, curr_temp))
        return result