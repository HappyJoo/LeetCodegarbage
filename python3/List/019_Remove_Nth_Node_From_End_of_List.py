# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left, right, index = head, head, 0
        while index < n:
            right = right.next
            index += 1
        if not right:  # When right is None, we have to remove the first node.
            return head.next
        while right.next:
            left, right = left.next, right.next
        left.next = left.next.next
        return head
        
            