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
        return s_ptr == len(s)


if __name__ == '__main__':
    s = 'abc'
    t = 'ahbgdc'
    e = True
    o = FinalSolution().isSubsequence(s, t)
    print(o)
    print(o == e)

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

    # Time: O(|T|)
    # Space: O(1)