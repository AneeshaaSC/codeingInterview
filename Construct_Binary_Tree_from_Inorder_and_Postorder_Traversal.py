# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if(len(inorder) < 1 or len(postorder) < 1):
            return None
        value = postorder.pop()
        root = TreeNode(value)
        index = inorder.index(value)
        root.right = self.buildTree(inorder[index+1::],postorder)
        root.left = self.buildTree(inorder[0:index],postorder)
        return root
