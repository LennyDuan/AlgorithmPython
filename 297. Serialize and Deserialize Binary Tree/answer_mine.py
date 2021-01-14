# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def build_res(root, res):
            if not root:
                res.append('#')
                return
            res.append(root.val)
            build_res(root.left, res)
            build_res(root.right, res)
            return res

        vals = build_res(root, [])

        print(vals)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        12##34##5##
        """
        res = []

        return res
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
