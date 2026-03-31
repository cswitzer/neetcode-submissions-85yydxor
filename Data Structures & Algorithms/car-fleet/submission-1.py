class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        pos => [1, 4]
        spe => [3, 2]
        positions => [(4, 2),(1, 3)]
        stack = [(4, 2), (1, 3)]

        front_time => (10 - 4) / 2 = 3
        back_time => (10 - 1) / 3 = 3

        # the car in the front reaches the 
        """
        stack = []
        positions = sorted(
            [(pos, speed) for pos, speed in zip(position, speed)],
            reverse=True,
        )

        for pos, speed in positions:
            stack.append((pos, speed))
            if len(stack) >= 2:
                # if the car before reaches the dest before the car in front...
                back_time = (target - stack[-1][0]) / stack[-1][1]
                front_time = (target - stack[-2][0]) / stack[-2][1]
                if back_time <= front_time:
                    stack.pop()
        return len(stack)