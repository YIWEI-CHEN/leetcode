# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InOrderSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(root):
            if root is None:
                return []
            stack = [root]
            seq = []
            while stack:
                node = stack.pop()
                if node is None:
                    seq.append(None)
                    continue
                seq.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                # seq.append(node.val)
                # if not node.left and not node.right:
                #     continue
                # if node.left is None:
                #     seq.append(None)
                # else:
                #     stack.append(node.left)
                # if node.right is not None:
                #     stack.append(node.right)
            return seq
        p_seq = preorder(p)
        q_seq = preorder(q)
        return p_seq == q_seq


class IntuitiveIterativeSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # intuitive comparison
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        queue = collections.deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            # p=[], q is not None or p is not None and q=[] will be checked
            if not check(p, q):
                return False
            if p is not None:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True
