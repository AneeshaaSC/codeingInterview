# Definition for a  binary tree node
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if (root == None):
            return []

        if (root.left == None and root.right == None):
            return [root.val]
        
        ListOfInt = []
        ListOfNode = []
        while (True):
            if (root.left !=None):
                ListOfNode.append([root,0])
                root = root.left
                continue
            
            if (root.left == None and root.right == None):
                ListOfInt.append(root.val)
                if(len(ListOfNode) > 0):
                    temp = ListOfNode.pop()
                    root = temp[0]
                    if (temp[1] == 0):
                        root.left = None
                    if (temp[1] == 1):
                        root.right = None
                else: return ListOfInt
                continue
                
            if (root.right != None and root.left == None):
                ListOfInt.append(root.val)
                if (len(ListOfNode) > 0):
                    if (ListOfNode[len(ListOfNode)-1][1]== 0):
                        ListOfNode[len(ListOfNode)-1][0].left = None
                    if (ListOfNode[len(ListOfNode)-1][1]== 1):
                        ListOfNode[len(ListOfNode)-1][0].right = None
                root = root.right
                continue
                
                
