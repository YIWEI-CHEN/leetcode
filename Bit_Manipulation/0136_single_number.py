"""
Single Number

Easy

Links:
1. NeetCode 150: https://neetcode.io/problems/single-number
2. LeetCode: https://leetcode.com/problems/single-number

You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with O(n) runtime complexity and use only O(1) extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        for k, v in h.items():
            if v == 1:
                return k


class Solution2:
    # worst than Solution1
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            if h.get(n) is None:
                h[n] = 1
            else:
                del h[n]
        return [*h][0]


class BitManipulationSolution:
    '''
    If we take XOR of zero and some bit, it will return that bit
    a^0 = a

    If we take XOR of two same bits, it will return 0
    a^a = 0

    a^b^a = (a^a)^b = 0^b = b

    Time complexity: O(n)
    Space complexity: O(1)
    
    Recommended solution
    '''
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


class Solution4:
    # 2∗(a + b + c)−(a + a + b + b + c) = c
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([3, 2, 3], 2),
        ([7, 6, 6, 7, 8], 8)
    ]
    
    print("Single Number Test Results:")
    print("=" * 50)
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = BitManipulationSolution().singleNumber(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {i}: {nums}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print("-" * 30)
