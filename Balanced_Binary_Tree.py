class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if(root == None):
            return True
        if(root.left == None and root.right == None): 
            return True
        left = self.helpFun(root.left) 
        right = self.helpFun(root.right )
        if (left.__class__ == type(True) or right.__class__ ==type(True)):
            return False
        result = left - right
        if (result == 0 or result == 1 or result == -1):
            return True
        else:
            return False
        
    
    def helpFun(self, root):
        if (root == None):
            height = 0
            return height
        if(root.left == None and root.right == None):
            height = 1
            return height

        
        left = self.helpFun(root.left)
        right = self.helpFun(root.right)
        if (left.__class__ == type(True) or right.__class__ ==type(True)):
            return False
        if (right - left == 0 or right - left == 1 or right - left == -1):
            height = max(left,right)+1
            return height
        else:
            height = max(left,right)+1
            return False

