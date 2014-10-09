# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if (l1 == None or l2 == None):
            if(l1 != None):
                return l1
            elif(l2 != None):
                return l2
            else:
                return None
        copyl1 = l1
        copyl2 = l2
        resultlist = ListNode(0)
        result = resultlist
        while(True):
            if( copyl1 == None):
                resultlist.next = copyl2
                return result.next
            if( copyl2 == None):
                resultlist.next = copyl1
                return result.next
                
            if(copyl1.val < copyl2.val):
                resultlist.next = ListNode(copyl1.val)
                copyl1 = copyl1.next
                resultlist = resultlist.next
            else:
                resultlist.next = ListNode(copyl2.val)
                copyl2 = copyl2.next
                resultlist = resultlist.next
