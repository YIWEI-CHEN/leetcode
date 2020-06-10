import collections


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        inverted_index = collections.defaultdict(list)
        for i, c in enumerate(source):
            inverted_index[c].append(i)
        cnt, next_pos = 1, -1

        def get_next(lst, pos):
            for e in lst:
                if e >= pos:
                    return e
            return None
        for c in target:
            if c not in inverted_index:
                return -1
            idx_list = inverted_index[c]
            next_pos = get_next(idx_list, next_pos)
            if next_pos is None:
                cnt += 1
                next_pos = idx_list[0] + 1
            else:
                next_pos += 1
        return cnt


if __name__ == '__main__':
    source = 'abcab'
    target = 'aabbaac'
    e = 3
    o = Solution().shortestWay(source, target)
    print(o)
    print(e == o)
    # subseq of source should be subseq of target
    # subseqs of source should be substrings of target

    # edge case
    # s='a', t='abc'
    # s='abc', t='c', 1
    # s='abcab', t='aabbaac'
    # s='abc', t='acdab'
    # s='abacb', t='aabbaac'

    # Time: O(|S| + log(|S|*|T|)
    # inverted idx: O(|S|)
    # get_next: O(|S|) linear search, if bisect search O(log(|S|))
    # Check target: O(|S|*|T|)
    # Space: O(|S|)
