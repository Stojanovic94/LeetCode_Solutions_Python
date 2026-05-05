# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        # Dummy node to simplify handling the new head
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # 1. Check if there are k nodes left to reverse
            kth_node = self.getKthNode(prev_group_end, k)
            if not kth_node:
                break
                
            next_group_start = kth_node.next
            
            # 2. Reverse the group
            prev, curr = next_group_start, prev_group_end.next
            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # 3. Connect the reversed group back to the list
            temp = prev_group_end.next
            prev_group_end.next = kth_node
            prev_group_end = temp
            
        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr        