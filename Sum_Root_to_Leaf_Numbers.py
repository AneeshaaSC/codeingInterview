# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if (root == None):
            return 0
        if (root.left == None and root.right == None):
            return root.val
        array = self.helper(root, 0 ,[])
        sum = 0
        for i in array:
            sum += i
        return sum
        
        
    def helper(self, root, result, array):
        result = result * 10 + root.val
        if (root.left == None and root.right == None):
            array.append(result)
            return array
        if (root.left != None):
            array = self.helper(root.left, result , array)
        if (root.right != None):
            array = self.helper(root.right, result , array)   
        return array
        
        
