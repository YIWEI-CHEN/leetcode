from typing import List


class WrongSolution:
    # costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    # ans = 1859
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        plan_a = self.plan(costs, 0)
        plan_b = self.plan(costs, 1)
        return plan_a if plan_a < plan_b else plan_b

    def plan(self, costs, city_idx):
        half_peo = int(len(costs) / 2)
        costs.sort(key=lambda x: x[city_idx])
        cost_a = sum(c[city_idx] for c in costs[:half_peo])
        cost_b = sum(c[1 - city_idx] for c in costs[half_peo:])
        return cost_a + cost_b


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        half = int(len(costs) / 2)
        costs.sort(key=lambda x: x[0] - x[1])
        cost_a = sum(c[0] for c in costs[:half])
        cost_b = sum(c[1] for c in costs[half:])
        return cost_a + cost_b


if __name__ == '__main__':
    # costs = [[10,20],[30,200],[400,50],[30,20]]
    # ans = 110
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    ans = 1859
    res = Solution().twoCitySchedCost(costs)
    print(res)