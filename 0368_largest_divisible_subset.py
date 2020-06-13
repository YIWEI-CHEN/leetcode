import collections
from typing import List


class WrongSolution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        dv = collections.defaultdict(list)

        max_len = 0
        max_subset = []
        for i in range(len(nums)):
            curr = nums[i]
            for n in nums[i:]:
                if curr % n == 0:
                    dv[curr].append(n)
            if len(dv[curr]) > max_len:
                max_len = len(dv[curr])
                max_subset = dv[curr]
        return max_subset

# Sort the list
# From large to small, check the rest of elements is divisible with current one, get the subset
# use two loop to examine all elements,
# Time: O(N^2)
# Space: O(N^2)
# Wrong answer without dynamic programming:

# edge
# [4, 8, 10, 240] --> [4, 8, 240]
# My wrong solution will give [4, 8, 10, 240]

class DPConciseSolution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dv = {-1: []}

        for n in sorted(nums):
            dv[n] = max([dv[k] for k in dv if n % k == 0], key=len) + [n]
        return list(max(dv.values(), key=len))


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dv = collections.defaultdict(list)

        max_len = 0
        max_subset = []
        for i in range(len(nums)):
            curr = nums[i]
            m = 0
            max_n = []
            for n in nums[:i]:
                if curr % n == 0 and len(dv[n]) > m:
                    m = len(dv[n])
                    max_n = dv[n]
            dv[curr] = max_n + [curr]
            if len(dv[curr]) > max_len:
                max_len = len(dv[curr])
                max_subset = dv[curr]
        return max_subset


if __name__ == '__main__':
    nums = [4, 8, 10, 240]
    e = [4, 8, 240]
    o = DPConciseSolution().largestDivisibleSubset(nums)
    o.sort()
    print(o)
    print(o == e)
