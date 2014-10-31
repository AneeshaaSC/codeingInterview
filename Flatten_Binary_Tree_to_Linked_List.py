# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if (root == None):
            return root
        if (root.left == None and root.right == None):
            return root
        lastNode = TreeNode(-1)
        self.helper(lastNode,root,[])

        
        
    def helper(self, lastNode, root, stack):
        if (root.left == None and root.right == None):
            if(len(stack) > 0):
                root.right = stack.pop()
                root.left = None
                self.helper(root, root.right, stack)
            return root
        
        if (root.right != None and root.left == None):
            self.helper(root,root.right, stack)
            
        if (root.right != None):
            stack.append(root.right)

        if (root.left != None):
            root.right = root.left
            root.left = None
            self.helper(root,root.right, stack)


        return root
        
