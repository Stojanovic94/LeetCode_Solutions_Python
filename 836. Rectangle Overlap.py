class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1_left, r1_right = rec1[0], rec1[2]
        r2_left, r2_right = rec2[0], rec2[2]
        x_overlap_left = max(r1_left, r2_left)
        x_overlap_right = min(r1_right, r2_right)

        r1_bottom, r1_top = rec1[1], rec1[3]
        r2_bottom, r2_top = rec2[1], rec2[3]
        y_overlap_bottom = max(r1_bottom, r2_bottom)
        y_overlap_top = min(r1_top, r2_top)

        x_overlap = x_overlap_right - x_overlap_left
        y_overlap = y_overlap_top - y_overlap_bottom

        return x_overlap > 0 and y_overlap > 0