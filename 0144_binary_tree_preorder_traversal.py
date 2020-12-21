# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        # stack, seq = [root], []
        # while stack:
        #     n = stack.pop()
        #     if n is None:
        #         continue
        #     seq.append(n.val)
        #     stack.append(n.right)
        #     stack.append(n.left)
        # return seq

        # recursive
        output = []

        def helper(node):
            if node is None:
                return
            output.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return output
