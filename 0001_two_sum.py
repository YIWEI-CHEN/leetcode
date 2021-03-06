from typing import List


class BFSolution1:
    # brute force solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if target == num + nums[j]:
                    return [i, j]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pass + hash
        h = dict()
        for i, n in enumerate(nums):
            h[n] = i
        for i, n in enumerate(nums):
            complement = target - n
            if complement in h and h[complement] != i:
                return [i, h[complement]]


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass + hash
        h = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in h:
                if h[complement] != i:  # redundant expression, so it comes to solution4
                    return [h[complement], i]
            else:
                h[n] = i


class GoodSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1 pass + hash: similar to solution 3, but no h[complement] != i
        '''
        nums = [3, 2, 4], target = 6
        3: 0
        2: 1
        '''
        h = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in h:
                return [h[complement], i]
            else:
                h[n] = i


class FinalSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash will save the complement and index, rather than saving original num
        '''
            nums = [3, 2, 4], target = 6
            3 -> 3: 0
            4 -> 2: 1
        '''
        h = {}  # save more time than dict()
        for i, n in enumerate(nums):
            if n in h:
                return [h[n], i]
            h[(target - n)] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    result = FinalSolution().twoSum(nums, target)
    print(result)
