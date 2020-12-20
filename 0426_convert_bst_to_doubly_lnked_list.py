"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        # Write your code here.
        stack = []
        current = root
        output = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                output.append(current)
                current = current.right
            else:
                break
        n_noeds = len(output)
        for i in range(n_noeds):
            successor = 0 if i + 1 == n_noeds else i + 1
            output[i].right = output[successor]
            output[i].left = output[i - 1]
        return output[0]
