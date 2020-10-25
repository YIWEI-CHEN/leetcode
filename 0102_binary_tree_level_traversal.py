# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# We have to save the depth in BFS
# If we face a new depth, extend the list
class IterativeSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # iterative
        if not root:
            return []
        q = collections.deque([(root, 0)])
        l = []
        while q:
            node, depth = q.popleft()
            if not node:
                continue
            if len(l) == depth:
                l.append([])
            l[depth].append(node.val)
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        return l


class RecursiveSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # recursive
        l = []
        def helper(root, depth):
            if not root:
                return
            if len(l) == depth:
                l.append([])
            l[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return l
