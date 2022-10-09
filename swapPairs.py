# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = newhead.next
        newhead.next = head
        head.next = self.swapPairs(head.next)
        return newhead
            
        