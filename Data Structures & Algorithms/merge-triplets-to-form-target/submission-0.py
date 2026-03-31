class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        If we can make a choice now that will NOT hurt getting the best answer
        or result in the future, use greedy!

        For example, if the problem has something like
        max, min, earliest, latest, intervals, then try greedy first

        If it has count ways, min cost, subset, exact value, DP is more likely

        If worse states can be discarded and not even considered, then greedy is likely.
        If they CANNOT be discarded, then DP is likely

        At every triplet, we KNOW that the triplet can never contribute meaningfully to reaching
        the target if we have a value that is greater than one of the values in target.
        When we go through the process of merging triplets (by taking the max), the only triplets that will
        contribute positively to reaching the target are those with values <= to the targets values.
        So:

        For each triplet, if x, y, or c is <= to any of the values in the target AND
        NONE of them surpass the corresponding values in target, then we know that triplet can contribute 
        positively to the final target
        """
        a, b, c = target
        a_seen, b_seen, c_seen = False, False, False

        for x, y, z in triplets:
            if x <= a and y <= b and z <= c:
                if x == a:
                    a_seen = True
                if y == b:
                    b_seen = True
                if z == c:
                    c_seen = True
        
        return a_seen and b_seen and c_seen
