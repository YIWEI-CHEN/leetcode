# Python program to print topological sorting of a DAG
# This code is contributed by Neelam Yadav

from collections import defaultdict

# Class to represent a graph


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order


def topological_sort(graph):
    adjacent = defaultdict(set)
    visited = set()
    nodes = set()
    for source, target in graph:
        adjacent[source].add(target)
        nodes.add(source)
        nodes.add(target)
    rv = []

    def recursive_sort_util(node):
        if node not in visited:
            visited.add(node)
            for target in adjacent[node]:
                recursive_sort_util(target)
            rv.append(node)

    for n in nodes:
        recursive_sort_util(n)
    return rv[::-1]


if __name__ == '__main__':

    # Driver Code
    # g = Graph(6)
    # graph = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

    g = Graph(4)
    graph = [(0, 1), (0, 2), (1, 3), (2, 3)]
    # graph = [(0, 1), (1, 2), (1, 3)]
    for s, t in graph:
        g.addEdge(s, t)

    print("Following is a Topological Sort of the given graph")

    # Function Call
    g.topologicalSort()

    rv = topological_sort(graph=graph)
    print(rv)

