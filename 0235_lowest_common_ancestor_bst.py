# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# According to the attribute of BST,
# If p, q are in the right subtree, its common ancestor must be in the right subtree
# If p, q are in the left subtree, its common ancestor must be in the right subtree
# If p and q are in different subtree, the node is the lowest common ancestor.


class IterativeSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative
        node = root
        while node:
            val = node.val
            if p.val > val and q.val > val:
                node = node.right
            elif p.val < val and q.val < val:
                node = node.left
            else:
                return node


class RecursiveSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursive
        val = root.val
        if p.val > val and q.val > val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < val and q.val < val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
