# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Given a linked list, determine if it has a cycle in it.

#Follow up:
#Can you solve it without using extra space?


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if (head == None or head.next == None):
            return False
        tempDict = dict()
        while (head != None):
            if(tempDict.has_key(id(head))):
                return True
            else:
                tempDict.update({id(head) : 0})
                head = head.next
            
            if (head.next == None):
                return False


