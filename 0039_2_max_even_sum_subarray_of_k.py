from functools import lru_cache


class Solution:
    def maxEvenSumSubarray(self, A, K) -> int:
        # A = set(A)
        evens = [n for n in A if n % 2 == 0]
        odds = [n for n in A if n % 2 == 1]
        evens.sort(reverse=True)
        odds.sort(reverse=True)
        m, n = len(evens), len(odds)

        @lru_cache(None)
        def dp(i, j, k):
            if k <= 0:
                return 0
            # choose even
            p1 = 0 if not i < m or k > m else dp(i + 1, j, k - 1) + evens[i]
            # choose odd
            p2 = 0 if not j < n - 1 or k < 2 else dp(i, j + 2, k - 2) + odds[j] + odds[j + 1]

            return max(p1, p2)

        ret = dp(0, 0, K)
        return -1 if ret == 0 else ret



if __name__ == '__main__':
    for A, K, expected in [
        ([4, 9, 8, 2, 6], 3, 18),
        ([5, 6, 3, 4, 2], 5, 20),
        ([7, 7, 7, 7, 7], 1, -1),
        ([10000], 2, -1),
        ([2, 3, 3, 5, 5], 3, 12),
    ]:
        ans = Solution().maxEvenSumSubarray(A, K)
        print(ans == expected)
