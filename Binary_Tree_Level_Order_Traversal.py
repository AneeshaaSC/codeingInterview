# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if (root == None):
            return []
        if (root.left == None and root.right == None):
            return [[root.val]]
        return self.helper(root,0,[])
        
        
        
    def helper(self,node,deapth,result):
        if (len(result) < deapth +1 ):
            result.append([])
        result[deapth].append(node.val)        

        
        if (node.left != None):
            result = self.helper(node.left,deapth+1,result)
            
        if(node.right != None):
            result = self.helper(node.right,deapth+1,result)
        
        return result
        
