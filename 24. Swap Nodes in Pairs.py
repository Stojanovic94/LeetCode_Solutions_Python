# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head

        pointer = head
        swapper = head.next

        pointer.next = swapper.next
        swapper.next = pointer

        head = swapper
        pointer = head.next
        while pointer:
            swapper = pointer.next
            if swapper and swapper.next:
                remain = swapper.next.next
                pointer.next = swapper.next
                pointer.next.next = swapper
                swapper.next = remain
            else:
                return head
            pointer = pointer.next.next
        return head

        