# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # The first element in preorder is the root node
        # The left side of the root node in the inorder will be the left subtree
        # The right side of the root node in the inorder will be the right subtree

        # 1. get root, decide sequence for left subtree and sequence for right subtree
        # 2. In the left sequence, repeat step1
        # 3. In the right sequence, repeat step1

        if len(inorder) == 0:
            return None
        root = TreeNode(val=preorder.pop(0))
        idx = inorder.index(root.val)
        left_seq, right_seq = inorder[:idx], inorder[idx + 1:]
        root.left = self.buildTree(preorder, left_seq)
        root.right = self.buildTree(preorder, right_seq)
        return root


class RecursiveHashSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # recursive with hash map
        def helper(start, end):
            if start >= end:
                return None
            root = TreeNode(val=preorder.pop(0))
            idx = idx_map[root.val]
            root.left = helper(start, idx)
            root.right = helper(idx + 1, end)
            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder))


class IterativeSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # inorder (LNR) can indicate that a node is the left or right subtree of the parent node
        # preorder (NLR) can ensure we can go to the deepest left subtree
        # "NL" of preorder means if a node is in left subtree, it must be the parent's left
        # "NR" of inorder means if a node is in the right subtree, it must be the bottemest element of stack's right.
        # iterative (hard to come up with...)
        if len(inorder) == 0:
            return None
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        root = TreeNode(preorder[0])
        stack = [root]
        for e in preorder[1:]:
            node = TreeNode(e)
            if idx_map[e] < idx_map[stack[-1].val]:
                stack[-1].left = node
            else:
                while stack and idx_map[e] > idx_map[stack[-1].val]:
                    u = stack.pop()
                u.right = node
            stack.append(node)
        return root
