from typing import List


class WrongSolution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n in [0, 1]:
            return
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        if i == 0:
            nums.reverse()
            return
        for j in range(n - 1, i, -1):
            if nums[j] >= nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]


class ConciseSolution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flag = True
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                # should use flag for i = 0, otherwise wrong output at [1,3,2] -> [2, 3, 1]
                flag = False
                break
        if flag:
            nums.reverse()
            return
        for j in range(n - 1, i, -1):
            # should use >, otherwise wrong output at [1,5,1] -> [1, 1, 5]
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]


if __name__ == '__main__':
    # nums = [1, 2, 7, 4, 3, 1]
    # expected = [1, 3, 1, 2, 4, 7]
    # nums = [3, 2, 1]
    # expected = [1, 2, 3]
    # nums = [1, 1, 1]
    # expected = [1, 1, 1]
    # nums = []
    # expected = []
    # nums = [1,3,2]
    # expected = [2,1,3]
    nums = [1,5,1]
    expected = [5,1,1]
    ConciseSolution().nextPermutation(nums)
    print(nums == expected)
