# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if (root == None):
            return []
        if (root.left == None and root.right == None):
            return [root.val]
        nodeStore = [[root,0]]
        result = []
        while(True):
            if(len(nodeStore) <1 ):
                break
            node = nodeStore[len(nodeStore)-1][0]
            path = nodeStore[len(nodeStore)-1][1]
            if (node.left != None and path == 0 ):
                nodeStore[len(nodeStore)-1][1] += 1
                nodeStore.append([node.left,0])
                continue
            elif (node.left == None and path == 0 ):
                nodeStore[len(nodeStore)-1][1] += 1
                
            if (node.right != None and path <= 1):
                nodeStore[len(nodeStore)-1][1] += 1
                nodeStore.append([node.right,0])
                continue
            result.append(node.val) 
            nodeStore.pop()
        return result
