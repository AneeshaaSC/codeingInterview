# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if (m == n):
            return head
        if (head == None):
            return None
        if (head.next == None):
            return None
        fakeHead = ListNode(-1)
        fakeHead.next = head
        temp = fakeHead
        array = []
        for i in range(1, m):
            temp = temp.next #may have wrong index
        start = temp
        for i in range(m,n+1):
            array.insert(0,temp.next)
            temp = temp.next
        temp = temp.next
        for i in range(len(array)):
            start.next = array[i]
            start = start.next
        start.next = temp
        return fakeHead.next


        
