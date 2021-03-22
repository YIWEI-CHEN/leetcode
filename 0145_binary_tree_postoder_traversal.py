# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        def helper(node):
            if node is None:
                return
            helper(node.left)
            helper(node.right)
            output.append(node.val)

        helper(root)
        return output


class IterativeSolution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        s1, s2 = [root], []
        output = []
        while s1:
            node = s1.pop()
            if node is None:
                continue
            s2.append(node)
            s1.append(node.left)
            s1.append(node.right)
        while s2:
            node = s2.pop()
            output.append(node.val)
        return output
