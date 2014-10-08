#Given a binary tree, return the preorder traversal of its nodes' values.
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if (root == None):
            return []
        if (root.left == None and root.right == None):
            return [root.val]
        rootCopy= root
        listOfNode = []
        listOfInt = []
        while(True):
            if (rootCopy.right != None):
                listOfNode.append(rootCopy.right)
            listOfInt.append(rootCopy.val)
            
            if (rootCopy.left != None):
                rootCopy = rootCopy.left
                continue
            
            if (rootCopy.right != None):
                if (listOfNode[len(listOfNode)-1] == rootCopy.right):
                    listOfNode.pop()
                rootCopy = rootCopy.right
                continue
            
            if (rootCopy.left == None and rootCopy.right == None):
                if(len(listOfNode) == 0):
                    return listOfInt
                else:
                    rootCopy = listOfNode.pop()
                    continue
            
            
