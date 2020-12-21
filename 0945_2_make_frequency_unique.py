import collections


class HashSolution:
    def maxFrequencyUnique(self, s) -> int:
        freq = list(collections.Counter(s).values())
        freq.sort(reverse=True)

        deletes, record = 0, {}
        def find(num):
            while num in record:
                num = record[num] - 1
                if num < 0:
                    return 0
            record[num] = num
            return num
        for num in freq:
            deletes += num - find(num)
        return deletes


class SortedSolution:
    def maxFrequencyUnique(self, s) -> int:
        freq = list(collections.Counter(s).values())
        freq.sort(reverse=True)

        deletes, need = 0, freq[0]
        for num in freq:
            deletes += max(num - need, 0)
            need = max(need - 1, 0)
        return deletes


if __name__ == '__main__':
    # s = 'aaaabbbb'
    # expected = 1

    # s = 'ccaaffddecee'
    # expected = 6
    #
    # s = 'eeee'
    # expected = 0
    #
    # s = 'example'
    # expected = 4

    for s, expected in [
        ('aaaabbbb', 1),
        ('ccaaffddecee', 6),
        ('eeee', 0),
        ('example', 4),
    ]:
        ans = SortedSolution().maxFrequencyUnique(s)
        print(ans == expected)
