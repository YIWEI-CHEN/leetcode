import collections
from typing import List


class BackTrackingSolution:
    # or also called DFS
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking(curr, curr_target, start):
            if curr_target < 0:
                return
            if curr_target == 0:
                ans.append(curr)
            for i in range(start, len(candidates)):
                backtracking(curr + [candidates[i]], curr_target - candidates[i], i)
        backtracking([], target, 0)
        return ans


# [2, 3, 6, 7]
# DFS: [7], [6], [6, 6], [6, 7], [3], [3, 3], [3, 6], ...
# End elements and their descendence will appear first
class IterativeDFSSolution:
    # or also called DFS
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = [([], target, 0)]
        while stack:
            curr, curr_target, start = stack.pop()
            for i in range(start, len(candidates)):
                c = candidates[i]
                new_target = curr_target - c
                if new_target == 0:
                    ans.append(curr + [c])
                elif new_target > 0:
                    stack.append((curr + [c], new_target, i))
        return ans


# [2, 3, 6, 7]
# BFS: [2], [3], [6], [7], [2, 2], [2, 3], [2, 6], [2, 7], etc.
# elements grow more as it iterates
class BFSSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        queue = collections.deque([([], target, 0)])

        while queue:
            curr, curr_target, start = queue.popleft()
            for i in range(start, len(candidates)):
                c = candidates[i]
                new_target = curr_target - c
                if new_target == 0:
                    ans.append(curr + [c])
                elif new_target > 0:
                    queue.append((curr + [c], new_target, i))
        return ans


# The Top-down is close to BackTrackingSolution
class TopDownSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dp(curr, remain):
            if remain < 0:
                return
            if remain == 0:
                ans.append(curr)
            for num in candidates:
                # avoid duplicate solutions, e.g., [[2, 2, 3], [2, 3, 2], [3, 2, 2]]
                if len(curr) > 0 and num < curr[-1]:
                    continue
                # stop when the candidate is bigger than current target
                if num > remain:
                    break
                dp(curr + [num], remain - num)

        dp([], target)
        return ans


class BottumUpSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize storage from 0 to target
        dp = [[[]]] + [[] for _ in range(target)]
        candidates.sort()

        for t in range(1, target + 1):
            for c in candidates:
                # stop when the candidate is bigger than current target
                if c > t:
                    break
                for sol in dp[t - c]:
                    # avoid duplicate solutions, e.g., [[2, 2, 3], [2, 3, 2], [3, 2, 2]]
                    if len(sol) > 0 and c < sol[-1]:
                        continue
                    dp[t].append(sol + [c])
        return dp[target]


class BriefBottumUpSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize storage from 0 to target
        dp = [[[]]] + [[] for _ in range(target)]

        # For each candidate, create valid lists from candidate to target
        # For each candidate, the corresponding combination sum "c to the target value"
        # The iteration order (c -> target) could avoid duplicate combination sums
        for c in candidates:
            for i in range(c, target + 1):
                dp[i] += [solution + [c] for solution in dp[i - c]]
        return dp[target]


if __name__ == '__main__':
    C = [2, 3, 6, 7]
    t = 7
    expected = [[2, 2, 3], [7]]
    ans = IterativeDFSSolution().combinationSum(C, t)
    print(ans == expected)
