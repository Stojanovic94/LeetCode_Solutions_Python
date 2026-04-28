class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # 1. Transform 2D points to 1D perimeter positions
        flat = []
        for x, y in points:
            if y == 0: flat.append(x)
            elif x == side: flat.append(side + y)
            elif y == side: flat.append(2 * side + (side - x))
            else: flat.append(3 * side + (side - y))
        
        flat.sort()
        n = len(flat)
        total_len = 4 * side
        
        # 2. Check function: Can we fit k points with min distance 'dist'?
        def check(dist):
            # Because it's circular, we try starting from different early points
            # (Usually checking the first point's gap is enough for this constraint)
            for start_idx in range(n):
                if flat[start_idx] > flat[0] + dist: break # Optimization
                
                count = 1
                curr_pos = flat[start_idx]
                first_pos = flat[start_idx]
                
                last_idx = start_idx
                for _ in range(k - 1):
                    # Find next point at least 'dist' away
                    target = curr_pos + dist
                    # Binary search to find the next valid point
                    idx = bisect_left(flat, target)
                    if idx == n: return False # Ran out of points
                    curr_pos = flat[idx]
                    last_idx = idx
                
                # Check if the last point is far enough from the first point (circular)
                if total_len - (flat[last_idx] - first_pos) >= dist:
                    return True
            return False

        # 3. Binary Search for the maximum possible minimum distance
        low, high = 0, total_len // k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans