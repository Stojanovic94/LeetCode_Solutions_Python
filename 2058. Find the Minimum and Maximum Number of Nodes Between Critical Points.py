class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        result = [-1, -1]
        min_distance = float('inf')

        previous_node = head
        current_node = head.next
        current_index = 1

        previous_current_index = 0
        first_current_index = 0

        while current_node.next is not None:

            # Check if current node is a critical point
            if ((current_node.val < previous_node.val and
                 current_node.val < current_node.next.val) or
                (current_node.val > previous_node.val and
                 current_node.val > current_node.next.val)):

                # First critical point
                if first_current_index == 0:
                    first_current_index = current_index
                    previous_current_index = current_index

                # Another critical point
                else:
                    distance = current_index - previous_current_index

                    min_distance = min(min_distance, distance)

                    previous_current_index = current_index

            # Move forward
            previous_node = current_node
            current_node = current_node.next
            current_index += 1

        # If we found at least two critical points
        if min_distance != float('inf'):

            max_distance = previous_current_index - first_current_index

            result[0] = min_distance
            result[1] = max_distance

        return result