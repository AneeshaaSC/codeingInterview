# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if (head == None):
            return head
        if (head.next == None):
            if(n == 1):
                head = None
                return head
            if(n == 2):
                return head.next
        temp=ListNode(0)
        temp.next = head
        self.helper(temp, 0 , n)
        return temp.next
        
    def helper(self, node, currentN, n):
            
        if (node.next != None):
            currentN = self.helper(node.next, currentN, n)
        else:
            return currentN + 1
        
        if (currentN == n):
            node.next = node.next.next

            
        return currentN + 1
        
