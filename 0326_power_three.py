import math
import sys


class SimpleSolution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


class LogSolution:
    def isPowerOfThree(self, n: int) -> bool:
        epsilon = sys.float_info.epsilon
        # print(math.log(n, 3))  # math.log(243, 3) = 4.999999999999999
        # print(math.log10(n) / math.log10(3))  # math.log10(243) / math.log10(3) = 5.0
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0
        # return n > 0 and (math.log10(n) / math.log10(3) + epsilon) % 1 <= 2 * epsilon


class FinalSolution:
    def isPowerOfThree(self, n: int) -> bool:
        # Assume integer is 4-byte
        max_int = 2**31 - 1
        max_power3 = int(math.log(max_int, 3))
        return n > 0 and 3 ** max_power3 % n == 0


if __name__ == '__main__':
    n = 243
    e = True
    o = FinalSolution().isPowerOfThree(n)
    print(o)
