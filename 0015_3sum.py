from typing import List


class WrongSolution:
    # Only consider one twoSum solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                idx = self.twoSum(nums[i + 1:], 0 - n)
                if idx is not None:
                    ret.append([nums[idx[0] + i + 1], nums[idx[1] + i + 1], n])
        return ret

    def twoSum(self, nums, target):
        h = dict()
        # Wrong
        for i, n in enumerate(nums):
            if n in h:
                return h[n], i
            else:
                h[target - n] = i
        return None


class HashSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, curr_idx, res):
        h = set()
        j = curr_idx + 1
        while j < len(nums):
            complement = -nums[curr_idx] - nums[j]
            if complement in h:
                res.append([nums[curr_idx], nums[j], complement])
                # avoid duplicated results
                while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                    j += 1
            h.add(nums[j])
            j += 1


class TwoPointerSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, curr_idx, res):
        low, high = curr_idx + 1, len(nums) - 1
        while low < high:
            s = nums[curr_idx] + nums[low] + nums[high]
            if s == 0:
                res.append([nums[curr_idx], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
            elif s < 0:
                low += 1
            else:
                high -= 1


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dup = set(), set()
        # res is set to avoid duplicated results
        for i, n in enumerate(nums):
            if n not in dup:
                dup.add(n)
                self.twoSum(nums[i + 1:], n, res)
        return res

    def twoSum(self, nums, val, res):
        seen = set()
        for n in nums:
            complement = -val - n
            if n in seen:
                # must use tuple for set and use "(...)" for sorted
                res.add(tuple(sorted((val, complement, n))))
            seen.add(complement)


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    # e = [[-1,-1,2],[-1,0,1]]
    nums = [0,0,0,0]
    e = [[0,0,0]]
    ans = Solution().threeSum(nums)
    print(ans == e)
