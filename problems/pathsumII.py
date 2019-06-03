# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root: return []

        res = []

        def dfs(root, path, sum):
            sum -= root.val  # visit curr
            currpath = path + [root.val]
            if sum == 0 and not root.left and not root.right:  # record
                res.append(currpath)
                return
            if root.left:
                dfs(root.left, currpath, sum)
            if root.right:
                dfs(root.right, currpath, sum)

        dfs(root, [], sum)
        return res