
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if (len(num)<1):
            return None

        root = TreeNode(num[len(num)/2])
        self.makeBalence(num,root,root,-1)
        return root
        
    def makeBalence(self, array, parentNode,currentNode,direction):
        if (len(array)<1):
            return
        if (currentNode == None):
            currentNode = TreeNode(array[len(array)/2])
            if (direction == 0):
                parentNode.left = currentNode
            if (direction == 1):
                parentNode.right = currentNode
        leftArray =array[0:len(array)/2] 
        rightArray=array[len(array)/2+1:]             
        self.makeBalence(leftArray,currentNode, currentNode.left,0)
        self.makeBalence(rightArray,currentNode, currentNode.right,1)
