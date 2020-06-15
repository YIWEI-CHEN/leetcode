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
