# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for i in lists:
            x = i
            while x:
                res.append(x.val)
                x = x.next

        def list_to_node(lst):
            if not lst:
                return None
            
            y = ListNode(lst[0])
            x = y
            for i in range(1, len(lst)):
                x.next = ListNode(lst[i])
                x = x.next
            return y

        return list_to_node(sorted(res))
    

        