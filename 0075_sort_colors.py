import collections
from typing import List


class Solution:
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


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    e = [0, 0, 1, 1, 2, 2]
    Solution().sortColors(nums)
    print(nums)
    print(nums == e)
