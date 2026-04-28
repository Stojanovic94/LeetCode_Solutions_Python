# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to help easily return the head of the resulting linked list
        curr = dummy        # Pointer to build the new linked list
        carry = 0           # Initialize carry to 0 for handling sums >= 10

        while l1 or l2 or carry:  # The "or carry" deals with edge case of adding carry when neither l1 or l2 are present 
            v1 = l1.val if l1 else 0  # Extract value from l1 if it exists, otherwise use 0
            v2 = l2.val if l2 else 0  # Extract value from l2 if it exists, otherwise use 0

            # Adding and finding carry
            val = v1 + v2 + carry     # Sum current digits and carry from previous step
            carry = val // 10         # Compute carry for the next digit (e.g., 15 -> carry = 1)
            val = val % 10            # Keep only the last digit (e.g., 15 -> val = 5)
            curr.next = ListNode(val) # Starting to add value to the dummy 

            # Updating carry
            curr = curr.next          # Move current pointer to the newly added node
            l1 = l1.next if l1 else None  # Move l1 pointer forward if it exists
            l2 = l2.next if l2 else None  # Move l2 pointer forward if it exists

        return dummy.next  # Return the next of dummy node, which is the head of the result list