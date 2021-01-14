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
        vals = []

        def build_res(root, res):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            build_res(root.left, res)
            build_res(root.right, res)

        build_res(root, vals)
        print(vals)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        12##34##5##
        """
        # queue = data.split(',')
        #
        # def build_tree(q):
        #     val = q.pop(0)
        #     if val == '#':
        #         return
        #     node = TreeNode(int(val))
        #     node.left = build_tree(q)
        #     node.right = build_tree(q)
        #     return node
        #
        # return build_tree(queue)
        vals = iter(data.split(','))
        def build_tree(vals):
            cur = next(vals)
            if cur == '#':
                return
            node = TreeNode(int(cur))
            node.left = build_tree(vals)
            node.right = build_tree(vals)
            return node

        return build_tree(vals)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
