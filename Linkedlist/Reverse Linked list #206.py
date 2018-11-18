''' 
To use linked list, first we should define a class Node to store the node's value and pointer.
Each node has its value val and pointer(position) : head.

The linked-list begins with the first node.
When we want to move to the next node, just use head = head.next.

Use two pointers, one at the current node, one at the previous node. 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = None
        while(head):
            cur = head          
            head = head.next
            cur.next = dummy 
            dummy = cur
        return dummy
