# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if (root == None):
            return 0
        if (root.left == None and root.right == None):
            return 1
        return self.helper(root, 1, 2147483647)
        
    def helper(self, root, currentDepth, result):
        if (root.left == None and root.right == None):
            return min(currentDepth, result)
            
        if (root.left != None):
            result = self.helper(root.left, currentDepth + 1, result)
        if (root.right != None):
            result = self.helper(root.right, currentDepth + 1, result)
        return result
             
