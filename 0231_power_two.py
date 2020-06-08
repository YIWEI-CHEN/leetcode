class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & -n == n


class FinalSolution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n-1) == 0

if __name__ == '__main__':
    n = 4
    e = True
    o = Solution().isPowerOfTwo(n)
    print(o)
    print(o == e)
