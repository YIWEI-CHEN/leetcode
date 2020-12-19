import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        n_5 = n // 5
        n_25 = n // 25
        n_125 = n // 125
        n_625 = n // 625
        n_3125 = n // 3125
        return n_5 + n_25 + n_125 + n_625 + n_3125


class FinalSolution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        power = int(math.log(n, 5))
        n_zeros = 0
        for p in range(power):
            n_zeros += n // (5 ** (p + 1))
        return n_zeros


if __name__ == '__main__':
    n = 3125
    e = 781
    ans = FinalSolution().trailingZeroes(n)
    print(e == ans)
