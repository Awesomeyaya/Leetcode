''' 
fast is as twice speed as slow

dummy is used to reverse the linked-list 

Anyway just remember it.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = None 
        fast = slow = head 
        while fast and fast.next:
            fast = fast.next.next
            dummy,dummy.next, slow= slow, dummy, slow.next
        if fast:
            slow = slow.next 
        while dummy and dummy.val == slow.val:
            slow = slow.next
            dummy = dummy.next
        return not dummy
            
