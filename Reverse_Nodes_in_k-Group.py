# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if ( k <= 1):
            return head
        temp = head
        for i in range(k):
            if (temp == None):
                return head
            temp = temp.next
            
        temp = head 
        tail = ListNode(temp.val)
        last = tail
        for i in range(k-1):
                next1 = ListNode(temp.next.val)
                next1.next = last
                newHead = next1 
                last = next1
                temp = temp.next
                
        if (temp.next != None):
            temp = temp.next
        else:
            return newHead       


        while(1):
            temp1 = temp
            for i in range(k-1):
                temp1 = temp1.next
                if (temp1 == None):
                    tail.next = temp
                    return newHead

            last = ListNode(temp.val)
            end = last
            for i in range(k-1):
                next1 = ListNode(temp.next.val)
                next1.next = last
                newHead1 = next1
                last = next1
                temp = temp.next
                
            tail.next = newHead1
            tail = end
            
            if (temp.next != None):
                temp = temp.next
            else:
                return newHead
          
        return newHead
