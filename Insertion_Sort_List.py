# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if (head == None):
            return None
        if(head.next == None):
            return head
        empty = ListNode(-1)
        empty.next = head
        beforef = empty
        first = head
	befores = empty.next
        second =head.next
        while (second != None):
            if (second == first):
                if (second.next != None):
                    if(second.next.val > second.val):
                        first = second
                        beforef = befores
                        second = second.next
                        befores = befores.next
                        continue 
                second = second.next
		befores = befores.next
                first = empty.next
                beforef = empty
		continue

            if (second.val < first.val):
		temp = second.next
                beforef.next = second
                second.next = first
		befores.next = temp	
		if(first.next == second):
			first.next = temp
		if (temp != None):
			if(temp.val > second.val):
				print "haha"
				first = second
				second = temp
				continue 
			
                second = temp
                first = empty.next
                beforef = empty
            else:
                first = first.next
                beforef = beforef.next
        return empty.next

def create(array):
	for i in range(len(array)):
		array[i] = ListNode(array[i])
	for i in range(len(array)-1):
		array[i].next = array[i+1]
	return array[0]
k = range(5000)[::-1]
b=Solution()
c =  b.insertionSortList(create(k))
	
while(c != None):
	print c.val
	c = c.next
