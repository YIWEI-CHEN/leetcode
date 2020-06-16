# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        q = collections.deque([root])
        while q:
            n = q.popleft()
            if n.val == val:
                return n
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
        return None
