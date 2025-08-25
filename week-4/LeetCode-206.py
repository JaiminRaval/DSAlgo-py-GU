class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev

            prev = curr
            curr = nextNode

        return prev
