# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def levelOrderBottom(self, root):
        if (root == None):
            return []
        if (root.left == None and root.right == None):
            return [[root.val]]
        return self.helper(root,0,[])
        
    def helper(self,node,level,result):
        if (node.left != None):
            result = self.helper(node.left,level +1,result )
        if (node.right != None):
            result = self.helper(node.right,level +1,result )   
        while(len(result) < level+1 ):
            result.insert(0,[])
        result[len(result) - level -1].append(node.val)
        return result
        
