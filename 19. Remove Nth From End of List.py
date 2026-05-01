# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of the list
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        # get index of the node to delete
        toDelete = length - n
        index = 0       # track the curr index
        
        curr = head
        prev = None
        nxt = curr.next
        while curr.next and index < toDelete:
            prev = curr
            curr = nxt
            nxt = curr.next
            index += 1
        
        # delete the curr node
        if toDelete == 0:
            return curr.next
        else:
            prev.next = nxt
            return head
        
        