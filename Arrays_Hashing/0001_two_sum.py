"""
Two Sum

Easy

Links:
1. NeetCode 150: https://neetcode.io/problems/two-integer-sum
2. LeetCode: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:
nums = [3,4,5,6], target = 7
Output: [0,1]

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

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


class HashMapOnePassSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        '''
        1 pass + hash: similar to solution 3, but no h[complement] != i

        nums = [3, 2, 4], target = 6
        map = diff -> index
        num:3, diff:3, idx:0
        num:2, diff:4, idx:1
        num:4, diff:2, idx:2

        Time complexity: O(n)
        Space complexity: O(n)

        Recommended solution
        '''
        prev_map = {} # diff -> idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            else:
                prev_map[n] = i


class HashMapOnePassEnhancedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        hash will save the complement and index, rather than saving original num
        nums = [3, 2, 4], target = 6
        3 -> 3: 0
        4 -> 2: 1

        Time complexity: O(n)
        Space complexity: O(n)

        '''
        h = {}  # save more time than dict()
        for i, n in enumerate(nums):
            if n in h:
                return [h[n], i]
            h[(target - n)] = i


if __name__ == '__main__':
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3, 4, 5, 6], 7, [0, 1]),
        ([4, 5, 6], 10, [0, 2]),
        ([1, 2, 3, 4, 5], 8, [2, 4]),
        ([-1, -2, -3, -4, -5], -8, [2, 4])
    ]
    
    print("Two Sum Test Results:")
    print("=" * 60)
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = HashMapOnePassSolution().twoSum(nums, target)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {i}: nums = {nums}, target = {target}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print("-" * 40)
