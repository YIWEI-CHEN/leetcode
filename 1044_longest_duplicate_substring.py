class TimeOutSolution:
    def longestDupSubstring(self, S: str) -> str:
        l = len(S)
        low, high = 1, l
        dup = []

        def has_dup_str(sub_len):
            h = {}
            has_dup = False
            end = l - sub_len + 1
            for i in range(0, end):
                sub_str = S[i:i + sub_len]
                if sub_str in h:
                    dup.append(sub_str)
                    has_dup = True
                else:
                    h[sub_str] = True
            return has_dup

        while low < high:
            mid = low + (high - low) // 2
            if has_dup_str(mid):
                low = mid + 1
            else:
                high = mid

        return max(dup, key=len) if dup else ''


if __name__ == '__main__':
    S = 'banana'
    e = 'ana'
    o = TimeOutSolution().longestDupSubstring(S)
    print(o)
    print(e == o)
    # initial ideas
    # hashmap
    # two pointer

    # S="banana"

    # char should repeat more than 1
    # s_ptr = b, repeated = 1, skip, move s_ptr
    # s_ptr = a, "a", repeated = 3, move p_ptr
    # p_ptr = n, "an", in S, repeated = 2
    # p_ptr = a, "ana" in S, repeated = 2
    # p_ptr = a, "anan" in S, repeated = 1, stop

    # Summary after reading the solution
    # Binary search by a string length to find the max_len of substring that has duplicate
    # Rabin-Karp using hash set a sliding window to check substring sequentially.

