'''
Tips:1. We don't have to count the lengths of the linked-list. We just need to set the condition of the while loop as (l1 or l2)
        In the while loop, we need to set the [if l1] and [ if l2] to select that whether the linked-list is vaild or None. 
        
     2. We use dummy and set it as the node before the first node. 
        dummy = cur = ListNode(0) : It is a standard expression for defining two pointers in a linked list.
        cur will change from cur.next. And the returned value is dummy.next.
     
     3. In the while loop, the cur.next is the number of the first node. Then cur points to cur.next. In this way, the numbers 
        calculated can be set to a new linked-list.
        
     4. cur.next = (l1.val + l2.val + carry) % 10 
        This is the number of each digit.
        carry = (l1.val + l2.val + carry) / 10 
        this is the carry bit.
        
     5. The returned linked-list is from dummy.next. 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0 
        while (l1 or l2 or carry):
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2: 
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next 
            carry = carry // 10 
        return dummy.next
