class Solution:
    def sortedArrayToBST(self, nums):
        def buil_tree(nums):
            if not nums:
                return
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = buil_tree(nums[:mid])
            node.right = buil_tree(nums[mid+1:])
            return node
        return buil_tree(nums)

