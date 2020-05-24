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


class Solution3:
    '''
    If we take XOR of zero and some bit, it will return that bit
    a^0 = a

    If we take XOR of two same bits, it will return 0
    a^a = 0

    a^b^a = (a^a)^b = 0^b = b
    '''
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a


class Solution4:
    # 2∗(a + b + c)−(a + a + b + b + c) = c
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    nums = [2, 2, 1]
    solution = Solution4().singleNumber(nums)
    print(solution)
