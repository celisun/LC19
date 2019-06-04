# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        low, high = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                return root
        return None