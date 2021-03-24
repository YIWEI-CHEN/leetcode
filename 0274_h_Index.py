from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if i + 1 >= c:
                return i + 1
        return len(citations)


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    e = 3
    ans = Solution().hIndex(citations)
    print(ans == e)