# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IterativeSolution:
    def maxDepth(self, root: TreeNode) -> int:
        # iterative
        if not root:
            return 0
        q = collections.deque([(root, 1)])
        max_depth = 0
        while q:
            node, depth = q.popleft()
            if not node:
                continue
            if depth > max_depth:
                max_depth = depth
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        return max_depth


class RecursiveBFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursive BFS
        max_depth = 0
        def helper(root, depth):
            nonlocal max_depth
            if not root:
                return
            if depth > max_depth:
                max_depth = depth
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 1)
        return max_depth


class RecursiveDFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursive DFS
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
