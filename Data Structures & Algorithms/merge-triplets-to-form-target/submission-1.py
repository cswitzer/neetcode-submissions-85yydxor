class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Greedy approach based on filtering valid contributors.
        
        Key observation:
        The merge operation takes the element-wise maximum of two triplets.
        This operation is monotonic — values can only increase and never decrease.

        Therefore:
        - If any triplet has a value greater than the target in any dimension,
        it can never be part of a valid solution (it would permanently exceed the target).
        - Such triplets can be safely discarded (greedy pruning).

        Strategy:
        - Iterate through all triplets.
        - Only consider "safe" triplets where each value is <= target.
        - Track whether we can match each dimension of the target exactly:
            - Have we seen a triplet with x == target[0]?
            - Have we seen a triplet with y == target[1]?
            - Have we seen a triplet with z == target[2]?

        If all three dimensions can be satisfied independently,
        then we can combine those triplets (via max) to form the target.

        Why greedy works:
        - Valid triplets never hurt the result.
        - Invalid triplets can be permanently discarded.
        - The merge operation is order-independent (associative and commutative).

        Time Complexity: O(n)
        Space Complexity: O(1)
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
