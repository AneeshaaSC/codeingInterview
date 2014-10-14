# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if (root == None):
            return True
            
        return self.symmetricHelp(root.left,root.right)
    
    def symmetricHelp(self, leftNode, rightNode):
        if (leftNode == None and rightNode == None):
            return True
        
        if (leftNode == None and rightNode != None):
            return False
        if (leftNode != None and rightNode == None):
            return False
    
        if (self.symmetricHelp(leftNode.left, rightNode.right) == False):
            return False
        if (leftNode.val != rightNode.val):
            return False
        if(self.symmetricHelp(leftNode.right, rightNode.left) == False):
            return False
        return True

        
