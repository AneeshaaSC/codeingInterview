# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if (head == None):
            return head
        if(head.next == None):
            return head
        temp = ListNode(0)
        temp.next = head
        result = temp
        index = 0
        nextNode = head.next
        self.findIt(temp, head, head.next,0)
        return result.next
        
        
    def findIt(self, parrent,currentNode, nextNode, index):
        if(nextNode == None):
            return
        if(index % 2 == 0):
            temp = nextNode.next
            parrent.next = nextNode
            nextNode.next = currentNode
            currentNode.next = temp
        self.findIt(parrent.next, parrent.next.next, parrent.next.next.next, index+1)

        
