'''
In this problem, we should define dummy and cur as a listNode(0). 
Let dummy points to the start of cur.
Everytime when we update cur.next, cur will move to cur.next.
And if the length of l1 and l2 is not equal, cur.next points to the left list l1 or l2.


Tips: 
It is like two pointers. But it is done with node.
''' 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1 
        head2 = l2 
        cur = dummy= ListNode(0)
        while head1 and head2: 
            if head1.val > head2.val: 
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head1.next 
            cur = cur.next
        cur.next = head1 or head2 
        return dummy.next
