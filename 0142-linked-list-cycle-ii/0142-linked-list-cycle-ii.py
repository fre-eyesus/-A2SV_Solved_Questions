# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            slow = head.next
            fast = head.next.next

            while fast and fast.next and fast != slow:
                fast = fast.next.next
                slow = slow.next

            if not fast or not fast.next:
                return None

            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None
        