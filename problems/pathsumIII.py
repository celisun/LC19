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
        :rtype: int
        """
        self.numofpath = 0
        self.dfs(root, [], sum)
        return self.numofpath

    def dfs(self, node, nums, sum):
        if not node: return
        # update all prev sums in dfs
        tmp = []
        for n in nums + [0]:
            tmp += [n + node.val]
            if n + node.val == sum: self.numofpath += 1  # a good sum
        self.dfs(node.left, tmp, sum)
        self.dfs(node.right, tmp, sum)