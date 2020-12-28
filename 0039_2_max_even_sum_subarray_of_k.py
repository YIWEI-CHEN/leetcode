from functools import lru_cache


class Solution:
    # Top-down solution
    # I have not come up with the bottum-up solution.
    # lru_cache can reduce the execution time of the function by using the memoization technique.
    # e.g., dp(k=1, odd=[], even=[2]) or dp(k=2, odd=[], even=[4, 2])
    def maxEvenSumSubarray(self, A, K) -> int:
        if K > len(A):
            return -1
        evens = [elmnt for elmnt in A if not elmnt & 1]
        odds = [elmnt for elmnt in A if elmnt & 1]
        evens.sort(reverse=True)
        odds.sort(reverse=True)
        m, n = len(evens), len(odds)

        @lru_cache(None)
        def dp(i, j, k):
            if k <= 0:
                return 0
            # choose even
            p1 = -1 if i >= m else dp(i + 1, j, k - 1) + evens[i]
            # choose odd
            p2 = -1 if k < 2 or j + 1 >= n else dp(i, j + 2, k - 2) + odds[j] + odds[j + 1]

            return max(p1, p2)

        return dp(0, 0, K)


# wrong solution for [2, 3, 3, 5, 5]
# because it did not consider [2, 5, 5]
def wrong_largest_even_sum3(arr, k):
    if len(arr) < k: return -1
    arr.sort()
    for i in range(len(arr))[::-1]:
        if i >= k - 1:
            res = 0
            n = k
            j = i
            while n > 0:
                res += arr[j]
                j -= 1
                n -= 1
            if not (res & 1):
                return res
        else:
            return -1


class RecursiveBackTrackingSolution:
    def maxEvenSumSubarray(self, A, K) -> int:
        if len(A) < K:
            return -1
        global res
        res = -1
        def backtrack(level, start, k):
            if k < 0:
                return
            lsum = sum(level)
            if k == 0 and not lsum & 1:
                global res
                res = max(res, lsum)
                return
            for i in range(start, len(A)):
                level.append(A[i])
                backtrack(level, i + 1, k - 1)
                level.pop()

        backtrack([], 0, K)
        return res


class IterativeBackTrackingSolution:
    pass


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
