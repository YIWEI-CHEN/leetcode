import math


class LogSolution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and math.log2(num) % 2 == 0


class BitSolution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0


class FinalSolution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1


if __name__ == '__main__':
    num = 5
    e = False
    o = FinalSolution().isPowerOfFour(num)
    print(o)
    print(e == o)