#Given two binary trees, write a function to check if they are equal or not.

#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        inOrderArrayForP = []
        posrOrderArrayForP = []
        inOrderArrayForQ = []
        posrOrderArrayForQ = []
        self.inOrder(p, inOrderArrayForP,1)
        self.inOrder(q, inOrderArrayForQ,1)
        self.postOrder(p, posrOrderArrayForP,1)
        self.postOrder(q, posrOrderArrayForQ,1)
        if ( inOrderArrayForP == inOrderArrayForQ and posrOrderArrayForP == posrOrderArrayForQ ):
            return True
        else:
            return False
        
        
    def inOrder(self, Node, array,direction):
        if (Node == None):
            array.append(None)
            return
 
        if (Node.left != None):
            self.inOrder(Node.left, array,1)
        array.append(Node.val+direction)
        if (Node.right != None):
            self.inOrder(Node.right, array,2)
        
    def postOrder(self, Node, array,direction):
        if (Node == None):
            array.append(None)
            return

        if (Node.left != None):
            self.postOrder(Node.left, array,1)
        if (Node.right != None):
            self.postOrder(Node.right, array,2)
        array.append(Node.val+direction)    
            
