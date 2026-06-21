class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        monotonic decreasing stack
        Keep adding while temperatures are decreasing
        When encountering a warmer temp, keep calculating result[i],
        which represents the numbers of days at i before a warmer temperature appears

        [30, 38, 30, 36, 35, 40, 28]
        at i = 1, pop 30
        at i = 1, get num days by subtracting i - prev_i
        """
        if len(temperatures) == 1:
            return [0]

        result = [0 for _ in range(len(temperatures))]
        stack = deque()
        stack.append((temperatures[0], 0))
        for i, t in enumerate(temperatures[1:], start=1):
            if stack[-1][0] >= t:
                stack.append((t, i))
            else:
                # found a warmer temperature
                while stack and t > stack[-1][0]:
                    prev_t, prev_i = stack.pop()
                    result[prev_i] = i - prev_i
                stack.append((t, i))
        return result