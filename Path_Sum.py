# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if (root == None):
            return False
        if (root.left == None and root.right == None):
            if (root.val == sum):
                return True
            else:
                return False
        return self.help(root,0,sum,False)
        
        
        
    def help(self, root, currentSum, sum, result):
        if (root.left != None):
            result = self.help(root.left, currentSum+root.val, sum, result )
            
        if (root.right != None):
            result = self.help(root.right, currentSum+root.val, sum, result )
            
        if (result == True):
            return True
            
        if (root.left == None and root.right == None):
            if (currentSum + root.val == sum):
                return True
            else:
                return False
        return result
            
            
