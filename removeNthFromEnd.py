# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        node_list = [head]
        cur = head
        l = 1
        while(cur):
            if cur.next:
                node_list.append(cur.next)
                l += 1
            cur = cur.next
        if l == n:
            if l > 1:
                return node_list[1]
            else:
                head = None
        if l - n + 1 < l:          
            node_list[l-n-1].next = node_list[l-n+1]
        else:
            node_list[l-n-1].next = None
        return head