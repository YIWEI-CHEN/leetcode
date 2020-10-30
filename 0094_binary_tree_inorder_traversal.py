# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IterativeOneLoopSolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # # iterative 1
        stack, output = [], []
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                output.append(current.val)
                current = current.right
            else:
                break
        return output


class IterativeTwoLoopSolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative 2: twice while lopp
        stack, output = [], []
        current = root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            output.append(current.val)
            current = current.right
        return output


class RecursiveSolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # recursive
        output = []
        def helper(root):
            if root is None:
                return
            if root.left is not None:
                helper(root.left)
            output.append(root.val)
            helper(root.right)
        helper(root)
        return output
