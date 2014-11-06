# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    head = ListNode(-1)
    def sortedListToBST(self, head):
        self.head = head
        return self.buildTree(head, self.count(head))


    def count(self, head):
        length = 0
        if (head != None):
            while(head.next != None):
                length += 1
                head = head.next
            if(head != None):
                length += 1
        
        return length
        
        
        
    def buildTree(self,head, length):
        if (length == 0):
            return None
        tempNode = TreeNode(-1)
        tempNode.left = self.buildTree(self.head,length/2)
        tempNode.val = self.head.val
        self.head = self.head.next
        tempNode.right = self.buildTree(self.head,length - length/2 -1)
        return tempNode
    
        
        
        
    
