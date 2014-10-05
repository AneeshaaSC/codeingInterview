#question:Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if (root == None):
            return 0
        if (root.left == None and root.right == None):
            return 1
            
        return self.findDepth(root)
        
        
    def findDepth(self, node):
        leftMax = 0
        rightMax = 0
        if (node.left == None and node.right == None):
            return 1
        
        if (node.left != None):
            leftMax = self.findDepth(node.left) +1
        
        if (node.right != None):
            rightMax = self.findDepth(node.right) +1
            
        return max(leftMax,rightMax)
        
