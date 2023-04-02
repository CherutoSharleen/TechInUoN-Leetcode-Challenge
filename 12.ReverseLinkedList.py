from typing import Optional, ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if not head or not head.next:
            return head
        curr, prev = head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

