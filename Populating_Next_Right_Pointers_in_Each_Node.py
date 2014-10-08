#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#Initially, all next pointers are set to NULL.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if(root == None):
            return None
        
        tempRoot = TreeNode(1)
        tempRoot.left = root
        self.helperFun(root,tempRoot)
        
        
    def helperFun(self,Node,parentNode):
        
        if (Node != parentNode.right):
            if (parentNode.right != None):
                Node.next = parentNode.right
            else:
                Node.next = None
        elif(parentNode.next != None):
            if (parentNode.next.left != None):
                Node.next =  parentNode.next.left
            elif(parentNode.next.right != None):
                Node.next =  parentNode.next.right
            else:
                Node.next = None
        else:
            Node.next = None
                
        
        if (Node.right != None):
            self.helperFun(Node.right, Node)       
        
        if (Node.left != None):
            self.helperFun(Node.left, Node)
        

