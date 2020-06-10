from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    e = 2
    o = Solution().searchInsert(nums, target)
    print(o)
    print(o == e)
    # binary search

    # edge case
    # nums = [], target = 1
    # nums = [1], target = 1
    # nums = [1], target = 5
    # nums = [6], target = 5
    # nums = [1, 2], target = 3
    # nums = [1, 3], target = 2
    # nums = [1,3,5,6], target = 5
    # nums = [1,3,5,6], target = 7

    # Time: O(log|num|)
    # Space: O(1)
