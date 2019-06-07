# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def transv(root, res):
            tmp = root.val - 1 # how many requires
            l = r = 0
            if root.left:
                l += transv(root.left, res)
            if root.right:
                r += transv(root.right, res)
            res[0] += abs(l) + abs(r)
            return tmp + l + r
        res = [0]
        transv(root, res)
        return res[0]