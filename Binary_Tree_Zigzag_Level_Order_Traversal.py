# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    result = []
    def zigzagLevelOrder(self, root):
        if (root == None) :
            return []
        if (root.left == None and root.right == None):
            return [[root.val]]
        self.result = []
        self.result.append([root.val])
        self.helper([root])
        return self.result
        
    def helper(self, treeArray):
        tempResult = []
        tempTreeArray = []
        for i in treeArray:
            if(i.left != None):
                tempResult.append(i.left.val)
                tempTreeArray.append(i.left)
            if(i.right != None):
                tempResult.append(i.right.val)
                tempTreeArray.append(i.right)
                
        if (tempResult == [] or tempTreeArray == []):
            return
        if(len(self.result) % 2 == 1):
            tempResult.reverse()
        self.result.append(tempResult)
        self.helper (tempTreeArray)
        
