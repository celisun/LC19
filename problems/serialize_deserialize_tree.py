# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return "#"
        tmp = [str(root.val)]
        tmp += [self.serialize(root.left)]
        tmp += [self.serialize(root.right)]
        return " ".join(tmp)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(" ")

        def decode(data):
            if not data: return None
            curr = data.pop(0)
            if curr == "#": return None
            node = TreeNode(curr)
            node.left = decode(data)
            node.right = decode(data)
            return node

        return decode(data)