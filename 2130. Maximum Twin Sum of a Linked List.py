# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head: return None
        # curr pointer adds the value of the current node to an array
        # The second moves 2x as fast. 
        # once the 2x as fast is at the end, the curr pointer is at half.
        # for the rest of curr, add value to array descending (reverse order)
        # return largest int in array
        curr = node = head
        hold = []
        while node:
            node = node.next
            if node:
                node = node.next
                hold.append(curr.val)
                curr = curr.next
        #print(f"hold: {hold[::-1]}, curr: {curr.val}")
        maxVal = -1
        for i in hold[::-1]:
            i += curr.val
            curr = curr.next
            if i > maxVal: maxVal = i
            #print(f"i: {i}")
        #print(f"hold: {hold}")
        return maxVal
                


        