class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Sort hand by asc order

        Concrete example:
        count = {1: 2, 2: 2, 3: 2}
        groupSize = 2

        freq of smallest element 1 is 2. If it was 0, this is no longer the smallest element and we
        must start with the next smallest

        Sort and process smallest card first — it has nowhere else to go, so every copy of it must start a new group.
        However many copies exist, consume that many from each of the next groupSize cards — because each copy needs its own complete group.
        If any card goes negative, return False — you needed more of a card than actually existed.
        """
        if len(hand) % groupSize != 0:
            return False

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

