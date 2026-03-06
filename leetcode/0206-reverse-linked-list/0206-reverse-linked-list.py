# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        cur = head
        if cur:
            while cur:
                ans.append(cur.val)
                cur = cur.next
        else:
            return None

        cur = head
        for h in ans[::-1]:
           cur.val = h
           cur = cur.next

        return head