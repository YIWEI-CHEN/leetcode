from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time: O(n), Space: O(n)
        # h = dict()
        # for i, n in enumerate(numbers):
        #     if n in h:
        #         return [h[n] + 1, i + 1]
        #     h[target - n] = i

        # # Time: O(n), Space: O(1)
        low, high = 0, len(numbers) - 1
        while low < high:
            s = numbers[low] + numbers[high]
            if s == target:
                return [low + 1, high + 1]
            if s < target:
                low += 1
            else:
                high -= 1


if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    e = [1,2]
    ans = Solution().twoSum(numbers, target)
    print(ans == e)
