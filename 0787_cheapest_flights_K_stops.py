import collections
import heapq
from typing import List


class WrongSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = [[None] * n] * n
        for src, dst, price in flights:
            adj[src][dst] = price

        curr_cost = [float("inf")] * n  # current cost from the source to each node
        curr_stops = [float("inf")] * n  # current stops from the source to each node
        curr_cost[src], curr_stops[src] = 0, 0

        min_heap = [(0, 0, src)]  # cost, stops, node
        while min_heap:
            cost, stops, node = heapq.heappop(min_heap)

            if node == dst:
                return cost

            if stops == K + 1:
                continue

            for neighbor in range(n):
                if adj[node][neighbor] is not None:
                    dU = cost  # current cost of the node
                    dV = curr_cost[neighbor]  # current cost from source to neighbor
                    wUV = adj[node][neighbor]  # price from node to the neighbor
                    if dU + wUV < dV:
                        curr_cost[neighbor] = dU + wUV
                        # curr_stops[stop] = stop + 1
                        heapq.heappush(min_heap, (dU + wUV, stops + 1, neighbor))
                    elif stops < curr_stops[neighbor]:
                        curr_stops[neighbor] = stops
                        heapq.heappush(min_heap, (dU + wUV, stops + 1, neighbor))
        return -1 if curr_cost[dst] == float("inf") else curr_cost[dst]


class Solution:
    '''
   minimum cost

   shortest path in terms costs

   1. construct the graph (map of node to adj nodes) - O(E)

   2. BFS - O(V + E)
   - initialize min_cost to infinity
   - in BFS queue put (node, stops, cost so far)
   - (do not stop at dest) when we reach dest just update the min cost to get to it and continue
   - When exceed k stops -> stop exploring neighboring
   - while exploring neighbours if going to that neighbour has cost > current min_cost
   - at the end if min_cost is still infinity (there's no path from s to d) so return -1

   m: nb of flights
   Time complexity: O(V + E) = O(n + m)
   Space complexity: O(V) = O(n)

   '''

    def findCheapestPrice(self, n: int, flights: List[List[int]], s: int, d: int, K: int) -> int:
        # 1.
        graph = collections.defaultdict(list)
        for u, v, c in flights:
            graph[u].append((v, c))

        queue = collections.deque([(s, 0, 0)])
        minCost = float('inf')
        while queue:
            node, stops, costSoFar = queue.popleft()
            if node == d:
                minCost = min(minCost, costSoFar)
                continue

            if stops > K or costSoFar > minCost:
                continue

            for nei, nc in graph[node]:
                queue.append((nei, stops + 1, costSoFar + nc))

        return minCost if minCost != float('inf') else -1


if __name__ == '__main__':
    # num = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # s = 0
    # d = 2
    # k = 1
    # e = 200
    num = 6
    flights = [[0, 1, 7], [0, 3, 5], [1, 4, 8], [3, 2, 3], [2, 4, 4], [4, 5, 5]]
    s = 0
    d = 4
    k = 2
    e = 12
    o = Solution().findCheapestPrice(num, flights, s, d, k)
    print(o)
    print(o == e)
