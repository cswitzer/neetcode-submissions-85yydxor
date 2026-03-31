class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        gas (the amount of gas at station i)
        cost (the amount of gas it takes to get to this station)

        gas  1, 2, 3, 4
        cost 2, 2, 4, 1

        interpretation
        station 1 fills 1 gas. It takes 2 gas to travel there
        station 2 fills 2 gas. It takes 2 gas to travel there
        station 3 fills 3 gas. It takes 4 gas to travel there
        station 4 fills 4 gas. It takes 1 gas to travel there

        starting at station 3, we will 3 gas.
        That is enough to travel to station 4.
        
        The formula to see if we can travel to the next gas station is:
        curr_gas + gas[i] - gas[i + 1]
        If the number is negative, we can no longer travel (we can keep traveling if current gas is 0)

        There seems to be a monotonic condition. We ONLY care if we have enough gas to travel to the next station
        starting at each index i
        """
        if sum(gas) < sum(cost):
            return -1

        total = 0
        result_index = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                # we have essentially proven that index from the initial start
                # to now (i) is impossible, so we must set a new starting position
                result_index = i + 1
        return result_index
        