class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Sort hand by asc order
        """
        counts = defaultdict(int)
        for card in hand:
            counts[card] += 1
        
        for card in sorted(counts):
            # try to build a new hand starting from the smallest available character
            # to size of groupSize 
            freq = counts[card]
            if freq == 0:
                continue
            for i in range(groupSize):
                counts[card + i] -= freq
                if counts[card + i] < 0:
                    return False
        return True

