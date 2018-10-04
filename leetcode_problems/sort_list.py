"""
/////////
Sort List
/////////

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5

Difficulty: MEDIUM
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        l = 0
        while temp != None:
            temp = temp.next
            l += 1

        if l <= 1:
            return head
        elif l == 2:
            if head.val <= head.next.val:
                return head
            else:
                temp = head.next
                head.next = None
                temp.next = head
                return temp
        m = l//2
        temp = head
        while m > 1:
            temp = temp.next
            m -= 1
        prev = temp
        temp = temp.next
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(temp)
        if right.val < left.val:
            temp = left
            left = right
            right = temp

        head = left
        temp = head
        left = left.next
        while right != None and left != None:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if right != None:
            temp.next = right
        if left != None:
            temp.next = left
        return head
