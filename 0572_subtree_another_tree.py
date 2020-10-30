# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class WrongBSTSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # Wrong solution BST
        # BST does not keep sub-tree structure in traversal
        def bst(root):
            q, output = collections.deque([root]), []
            while q:
                n = q.popleft()
                if n is None:
                    output.append('None')
                else:
                    output.append('#{}'.format(n.val))
                    q.append(n.left)
                    q.append(n.right)
            return ''.join(output)
        s_seq, t_seq = bst(s), bst(t)
        return t_seq in s_seq


class WrongCompareSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # Wrong: s=[1, 1] and t=[1]
        def isIdentical(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val and isIdentical(n1.left, n2.left) and isIdentical(n1.right, n2.right)
        q = collections.deque([(s, t)])
        while q:
            n_s, n_t = q.popleft()
            if n_s is None or n_t is None:
                continue
            if n_s.val == n_t.val:
                return isIdentical(n_s, n_t)
            else:
                q.append((n_s.left, n_t))
                q.append((n_s.right, n_t))
        return False


class WrongInOrderSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # inorder: wrong s=[4,1,null,null,2] (in: LN #1 LN #2 RN #4 RN), t=[1,null,4,2] (in: LN #1 LN #2 RN #4 RN)
        def inorder(root):
            current = root
            prefix = ''
            seq, stack = [], []
            while True:
                if current is not None:
                    stack.append((current, prefix))
                    current = current.left
                    prefix = 'l'
                elif stack:
                    seq.append('{}None'.format(prefix))
                    current, prefix = stack.pop()
                    seq.append('#{}'.format(current.val))
                    current = current.right
                    prefix = 'r'
                else:
                    seq.append('{}None'.format(prefix))
                    break
            return ''.join(seq)

        s_seq, t_seq = inorder(s), inorder(t)
        return t_seq in s_seq


class PreOrderSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # preorder:
        def preorder(root):
            stack = [root]
            seq = []
            while stack:
                n = stack.pop()
                if n is not None:
                    seq.append('#{}'.format(n.val))
                    stack.append(n.right)
                    stack.append(n.left)
                else:
                    seq.append('None')
            return ''.join(seq)

        s_seq, t_seq = preorder(s), preorder(t)
        return t_seq in s_seq


class PostOrderSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # postorder:
        def postorder(root):
            s1, s2 = [root], []
            seq = []
            while s1:
                n = s1.pop()
                s2.append(n)
                if n is not None:
                    s1.append(n.left)
                    s1.append(n.right)
            while s2:
                n = s2.pop()
                if n is not None:
                    # seq.append('#{}'.format(n.val))
                    # wrong s=[12] (nn#12), t=[1] (nn#1)
                    seq.append('{}#'.format(n.val))
                else:
                    seq.append('None')
            return ''.join(seq)

        s_seq, t_seq = postorder(s), postorder(t)
        return t_seq in s_seq


class RecursiveEqualRecursivePreorderSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # recursive equals and recurise preorder
        def equals(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val and equals(n1.left, n2.left) and equals(n1.right, n2.right)

        def preorder(root):
            if equals(root, t):
                return True
            if root is not None:
                left = preorder(root.left)
                right = preorder(root.right)
                return left or right
            else:
                return False

        return preorder(s)


class RecursiveEqualIterativePreorderSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # recursive equals and iterative preorder
        def equals(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val and equals(n1.left, n2.left) and equals(n1.right, n2.right)

        stack = [s]
        while stack:
            n = stack.pop()
            if equals(n, t):
                return True
            if n is None:
                continue
            stack.append(n.right)
            stack.append(n.left)
        return False
