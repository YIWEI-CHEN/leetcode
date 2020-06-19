from typing import List


class WrongSolution:
    def hIndex(self, citations: List[int]) -> int:
        total_papers = len(citations)
        hidx = total_papers
        if total_papers == 0:
            return hidx

        for hidx in range(total_papers, -1, -1):
            num = 0
            low, high = 0, total_papers - 1
            while low < high:
                mid = low + (high - low) // 2
                if citations[mid] >= hidx:   # condition is wrong for [1,1,2,2]
                    low = mid + 1
                    num += 1
                else:
                    high = mid
            if citations[total_papers - 1] >= hidx and num >= hidx - 1:
                break
        return hidx


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        total_papers = len(citations)
        hidx = total_papers

        if total_papers == 0:
            return hidx

        for hidx in range(total_papers, -1, -1):
            low, high = 0, total_papers - 1
            mid = low + (high - low) // 2
            while low < high:
                if citations[mid] < hidx:
                    low = mid + 1
                else:
                    high = mid
                mid = low + (high - low) // 2
            if citations[mid] >= hidx and total_papers - mid >= hidx:
                break
        return hidx


class LeetCodeSolution:
    def hIndex(self, citations):
        """
        H-index >= total_papers - article index
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if citations[pivot] == n - pivot:
                return n - pivot
            elif citations[pivot] < n - pivot:
                left = pivot + 1
            else:
                right = pivot - 1

        return n - left


if __name__ == '__main__':
    citations = [0,1,4,5,6]
    e = 2
    # citations = [0, 1]
    # e = 1
    # citations = [1, 1, 2, 2]
    # e = 2
    o = LeetCodeSolution().hIndex(citations)
    print(o)
    print(e == o)
    # Binary Search
    # Edge  cases
    # []
    # hidx = 0

    # [0]
    # hidx = 1 no
    # hidx = 0 yes

    # [1]
    # hidx = 1 yes

    # [0, 0]
    # hidx = 2
    # hidx = 1
    # hidx = 0 yes

    # [1, 1]
    # hidx = 2  no
    # hidx = 1  yes

    # [0, 1, 2]
    # hidx = 3, no
    # hidx = 2, no
    # hidx = 1, yes

    # [0, 2, 8, 16]
    # hidx = 4  no
    # hidx = 3  no
    # hidx = 2  yes