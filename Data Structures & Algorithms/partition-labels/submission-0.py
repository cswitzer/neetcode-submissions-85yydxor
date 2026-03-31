class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Here is the key:

        Track the last index of all elements in the string
        While iterating through the string, keep track of the end.

        For example, in xyxxyz, the vars will come out as so:
        map = {x: 3, y: 4, z: 5}
        
        Iterations:
        i = 0 -> end = 3
        i = 1 -> end = max(3, 4) = 4
        i = 2 -> end = max(4, 3) = 4
        i = 3 -> end = max(4, 3) = 4
        i = 4 -> i == 4 is true, so add len of current substring to result (4 + 1)
        i = 5 -> end = max(4, 5) = 5. i == end is true, so add ((end + 1) - res[i - 1] or 0)

        In essense, we delay the cut until no character can escape in the future

        Time Complexity: O(n)
        Space Complexity: O(n) (the map)
        """
        result = []
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])
            if i == end:
                result.append(size)
                size = 0
        return result

