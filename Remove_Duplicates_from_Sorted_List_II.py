# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        empty = ListNode(-9999999)
        empty.next = head
        before = empty
        temp = empty
        NoAdd = empty
        while(head != None):
            if(temp.val == head.val):
                NoAdd = temp
                before.next = head.next
            elif (temp !=None):
                if (temp.val != head.val and temp.val != NoAdd.val):
                    before.next = temp
                    before = before.next
                
            temp = head 
            head = head.next 
            
        return empty.next
                
