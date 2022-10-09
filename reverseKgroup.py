# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l, node = 0, head
        while node and l != k:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        head.next = self.reverseKGroup(cur,k)
        return node
        
    def reserve(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)
        