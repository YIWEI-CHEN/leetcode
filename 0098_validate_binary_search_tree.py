# The smallest value in right subtree should be larger than the node's value --> valild
# The largest value in the left subtree should be smaller than the node's value --> valid
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        # DFS: put node, right, left in order to a stack
        # left subtree's upper bound is the current node's val
        # right subtree's lower bound is the current node's val
        if root is None:
            return True
        stack = [(root, float('-inf'), float('inf'))]  # node, lower, upper
        while stack:
            n, lower, upper = stack.pop()
            if n is None:
                continue
            val = n.val
            if val >= upper or lower >= val:
                return False
            stack.append([n.right, val, upper])
            stack.append([n.left, lower, val])
        return True


class InOrderSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        # DFS + in-order, will convert a BST to a ascending sorted sequece
        # If the sequece is not sorted, the BST is invalid
        # Key point for DFS implementation is to push node to the stack until the node's left is None
        # Then pop the stack and push the popped node's right to the stack until its left is None
        stack, last_element = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= last_element:
                return False
            last_element = node.val
            root = node.right
        return True


class SingleLoopInOrderSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        # DFS + in-order, will convert a BST to a ascending sorted sequece
        # If the sequece is not sorted, the BST is invalid
        # Key point for DFS implementation is to push node to the stack until the node's left is None
        # Then pop the stack and push the popped node's right to the stack until its left is None
        stack, last_element = [], float('-inf')
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if current.val <= last_element:
                    return False
                last_element = current.val
                current = current.right
            else:
                break
        return True
