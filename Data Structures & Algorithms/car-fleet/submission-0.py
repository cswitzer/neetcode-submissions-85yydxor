class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position and speed array both len n
        
        pos[i]   => position of ith car (in miles)
        speed[i] => speed of the ith car (in mph)

        target is position all cars are to meet at (in miles)
        return the number of car fleets that will arrive at the destination
        """
        pair = [(p, s) for p, s in zip(position, speed)]

        stack = deque()
        for p, s in sorted(pair)[::-1]:
            # calculate the total time the car will take to reach the target position
            time_to_target = ((target - p) / s)
            stack.append(time_to_target)

            # see if the current vehicle would reach the dest BEFORE the veh in front of it
            # which means a fleet will be formed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)