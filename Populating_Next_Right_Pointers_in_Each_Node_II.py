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
        if (root == None):
            return root
        if (root.left == None and root.right == None):
            return root
        self.helper(root, None, -1)
        return root
        
    def helper(self, root, father, direction):
        if(direction == 0):
            if(father.right != None):
                root.next = father.right
            else:
                while (father.next != None):
                    if (father.next.left != None):
                        root.next = father.next.left
                        break
                    elif (father.next.right != None):
                        root.next = father.next.right
                        break
                    else:
                        father = father.next
                
        if(direction == 1):
            if(father.next != None):
                if (father.next.left != None):
                    root.next = father.next.left
                elif (father.next.right != None):
                    root.next = father.next.right
                else:
                    while (father.next != None):
                        if (father.next.left != None):
                            root.next = father.next.left
                            break
                        elif (father.next.right != None):
                            root.next = father.next.right
                            break
                        else:
                            father = father.next
            else:
                root.next = None

        if (root.right != None):
            self.helper(root.right, root, 1)
        if (root.left != None):
            self.helper(root.left, root, 0)          


        
