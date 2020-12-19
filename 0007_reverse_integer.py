class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        max_int = 2 ** 31 - 1
        min_int = 2 ** 31 * -1
        if x < 0:
            sign, x = -1, x * -1
        while x != 0:
            pop = x % 10
            x = x // 10
            rev = rev * 10 + pop
            if rev >= max_int or rev * sign <= min_int:
                return 0
        return rev * sign


class FinalSolution:
    def reverse(self, x: int) -> int:
        rev = 0
        n = abs(x)
        max_int = 2 ** 31 - 1
        while n != 0:
            pop = n % 10
            n = n // 10
            rev = rev * 10 + pop
            if rev >= max_int:
                return 0
        return rev * -1 if x < 0 else rev


if __name__ == '__main__':
    # x = 123
    # e = 321
    x = -123
    e = -321
    ans = FinalSolution().reverse(x)
    print(ans == e)
