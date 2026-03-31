# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        middle = len(pairs) // 2
        left = self.mergeSort(pairs[:middle])
        right = self.mergeSort(pairs[middle:])

        return self.merge(left, right)

    def merge(self, left: List[Pair], right: List[Pair]):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result