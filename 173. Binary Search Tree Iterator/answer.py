class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    arr = []
    index = 0

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self.arr.append(node.val)
        self._inorder(node.right)

    def __init__(self, root: TreeNode):
        self.arr = []
        self.index = 0
        self._inorder(root)
        print(self.arr)

    def next(self) -> int:
        res = self.arr[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index < len(self.arr)

        # Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()