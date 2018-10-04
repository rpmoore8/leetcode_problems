"""
///////////////
Add Two Numbers
///////////////

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Difficulty: MEDIUM
"""


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
        temp = ListNode(0)
        lSum = temp
        carry = 0
        while (l1 != None and l2 != None):
            temp.next = ListNode(l1.val + l2.val + carry)
            temp = temp.next
            if temp.val > 9:
                temp.val %= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            temp.next = ListNode(l1.val + carry)
            carry = 0
            temp = temp.next
            if temp.val > 9:
                temp.val %= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next

        while l2 != None:
            temp.next = ListNode(l2.val + carry)
            carry = 0
            temp = temp.next
            if temp.val > 9:
                temp.val %= 10
                carry = 1
            else:
                carry = 0
            l2 = l2.next

        if carry > 0:
            temp.next = ListNode(carry)

        return lSum.next
