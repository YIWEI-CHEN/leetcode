import collections
from typing import List


class CountSolution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = collections.defaultdict(int)
        for n in nums:
            cnt[n] += 1
        idx = 0
        for color in range(3):
            count = cnt[color]
            for _ in range(count):
                nums[idx] = color
                idx += 1


class OnePassSolution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0  # leftmost of zero
        p2 = len(nums) - 1  # rightmost of zero
        curr = 0

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


if __name__ == '__main__':
    # nums = [2,0,2,1,1,0]
    # e = [0, 0, 1, 1, 2, 2]
    nums = [1, 2, 0]
    e = [0, 1, 2]
    OnePassSolution().sortColors(nums)
    print(nums)
    print(nums == e)
