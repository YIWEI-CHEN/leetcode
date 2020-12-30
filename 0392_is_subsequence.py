import bisect
import collections


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        s_ptr = 0
        t_ptr = 0
        while t_ptr < len(t):
            if s_ptr < len(s) and t[t_ptr] == s[s_ptr]:
                s_ptr += 1
            t_ptr += 1
        return s_ptr == len(s)


class FinalSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if len(s) == 0:
        #     return True
        # if len(t) == 0:
        #     return False
        # The above edge cases are in the while condition
        s_ptr, t_ptr = 0, 0
        while t_ptr < len(t) and s_ptr < len(s):
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
            t_ptr += 1
        # check the s_ptr move to the end.
        return s_ptr == len(s)


class BottomUpDPSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        sub_str_table = [[True] * (m + 1)] + [[False] * (m + 1) for _ in range(n)]
        for i, s_char in enumerate(s, start=1):
            for j, t_char in enumerate(t, start=1):
                if s_char == t_char:
                    sub_str_table[i][j] = sub_str_table[i - 1][j - 1] & True
                else:
                    sub_str_table[i][j] = sub_str_table[i][j - 1]
        return sub_str_table[n][m]


class TopDownDPSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        def dp(s_end, t_end):
            if s_end < 0:
                return True
            if t_end < 0:
                return False
            if s[s_end] == t[t_end]:
                return dp(s_end - 1, t_end - 1)
            else:
                return dp(s_end, t_end - 1)

        return dp(n - 1, m - 1)


class HashSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d = collections.defaultdict(list)
        for i, c in enumerate(t):
            d[c].append(i)

        curr = -1
        for c in s:
            if not c in d:
                return False
            l = d[c]
            p = bisect.bisect_left(l, curr)
            if p == len(l):
                return False
            curr = l[p] + 1
        return True


if __name__ == '__main__':
    # s, t, expected = 'abc', 'ahbgdc', True
    s, t, expected = 'bac', 'ahbgdca', False
    # s, t, expected = '', 'abc', True
    # s, t, expected = 'abc', '', False
    # s, t, expected = 'b', 'efg', False

    o = HashSolution().isSubsequence(s, t)
    print(o == expected)

    # hash of T
    # examine sequence order of s from end to start
    # complicate than two pointer method
    # s = "abc",
    # t = "ahbgdc"

    # edge cases
    # s = '', t = 'abc', True
    # s = 'abc', t = '', False
    # s = 'a', t='a'
    #  s= 'ab', t='abca'
    # s = 'b', t='efg'

    # Two Pointers Solution
    # Time: O(|T|)
    # Space: O(1)
