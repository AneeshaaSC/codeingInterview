# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if (len(preorder) < 1 or len(inorder) < 1):
            return None
        value = preorder[0]
        preorder.remove(value)
        index = inorder.index(value)
        root = TreeNode(value)
        root.left =  self.buildTree(preorder, inorder[0:index])
        root.right = self.buildTree(preorder, inorder[index+1 ::])
        return root
