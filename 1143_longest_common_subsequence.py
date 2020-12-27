class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        common_length = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(text1, start=1):
            for j, y in enumerate(text2, start=1):
                common_length[i][j] = common_length[i - 1][j - 1] + 1 if x == y else max(common_length[i][j - 1],
                                                                                         common_length[i - 1][j])
        return common_length[n][m]
