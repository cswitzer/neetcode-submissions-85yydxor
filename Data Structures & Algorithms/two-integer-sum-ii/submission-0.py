class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            potential_target = numbers[L] + numbers[R]
            if numbers[L] < numbers[R] and potential_target == target:
                return [L + 1, R + 1]
            if potential_target < target:
                L += 1
            else:
                R -= 1