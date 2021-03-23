import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IterSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.right is not None:
                q.append(node.right)
            if node.left is not None:
                q.append(node.left)
            self.swap(node)
        return root

    def swap(self, node):
        tmp = node.left
        node.left = node.right
        node.right = tmp


class FinalSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        q = collections.deque([root])
        while q:
            n = q.popleft()
            left, right = n.left, n.right
            # if left is None and right is None:
            #     continue
            if right is not None:
                q.append(right)
            if left is not None:
                q.append(left)
            n.left, n.right = right, left

        return root

class ConciseIterationSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])
        while q:
            n = q.popleft()
            if n is None:
                continue
            left, right = n.left, n.right
            q.append(left)
            q.append(right)
            n.left, n.right = right, left
        return root


class RecursiveSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        if root.right is not None:
            self.invertTree(root.right)
        if root.left is not None:
            self.invertTree(root.left)
        self.swap(root)
        return root

    def swap(self, node):
        tmp = node.left
        node.left = node.right
        node.right = tmp


class BetterRecursiveSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        if left is None and right is None:
            return root
        root.left = right
        root.right = left
        return root


class ConciseRecursiveSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
