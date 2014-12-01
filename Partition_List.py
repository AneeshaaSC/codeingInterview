# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if(head == None):
            return head
        
        leftSide = ListNode(-1)
        rightSide = ListNode(-1)
#        lastHead = ListNode(-1)

        temp = self.helper(head, leftSide, rightSide, x)
        temp.next = rightSide.next
        return leftSide.next
      
    def helper(self, head, left, right, x):
        if(head == None):
            right.next = None
            return left
        if (head.val < x ):
            left.next = head
            return self.helper(head.next, left.next, right, x)
        else:
            right.next = head
            return self.helper(head.next, left, right.next, x)     
         
         
