# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    result = []
    def pathSum(self, root, sum):
        if(root == None):
            return []
        self.result = []
        self.helper(root,[], 0,sum)
        return self.result
        
    def helper(self, root, array,currentSum, sum):
        array.append(root.val)
        copyArray = []+array
        currentSum += root.val
        if (root.left == None and root.right == None and currentSum ==sum):
            self.result.append(array)
            return 
        if (root.left!= None):
            self.helper(root.left, array, currentSum, sum)
        if (root.right!= None):
            self.helper(root.right, copyArray, currentSum, sum)
            
            
