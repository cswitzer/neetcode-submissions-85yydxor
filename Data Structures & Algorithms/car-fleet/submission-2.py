class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        pos => [1, 4]
        spe => [3, 2]
        positions => [(4, 2),(1, 3)]
        stack = [(4, 2), (1, 3)]

        front_time => (10 - 4) / 2 = 3
        back_time => (10 - 1) / 3 = 3

        # the car in the front 
        """
        stack = deque()
        positions = sorted(
            [(pos, speed) for pos, speed in zip(position, speed)],
            reverse=True
        )
        for pos, speed in positions:
            stack.append((pos, speed))
            if len(stack) >= 2:
                front_pos, front_speed = stack[-2]
                back_pos, back_speed = stack[-1]
                
                # if the car
                front_time = (target - front_pos) / front_speed
                back_time = (target - back_pos) / back_speed
                if back_time <= front_time:
                    stack.pop()
        return len(stack)