tion for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if(head == None):
            return None
        headCopy = head
        empty = RandomListNode(-1)
#        empty.next = RandomListNode(head.label)
        temp = empty
        while ( head!= None):
            temp.next = RandomListNode(head.label)
            temp = temp.next
            head=head.next
        
        temp = empty.next
        dictory = {}
        while( temp != None):
            dictory.update({temp.label: temp})
            temp=temp.next
        temp = empty.next
        
        while ( headCopy != None and temp != None):
            if (headCopy.random != None):
                listNode = dictory.get(headCopy.random.label)
                temp.random = listNode
            
            headCopy = headCopy.next
            temp = temp.next
        return empty.next
            
