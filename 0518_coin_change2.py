from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount_combs = [0 for _ in range(amount)]
        amount_combs.insert(0, 1)
        for c in coins:
            for a in range(c, amount + 1):
                amount_combs[a] += amount_combs[a - c]
        return amount_combs[amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    expected = 4
    output = Solution().change(amount, coins)
    print(output)
    print(output == expected)
