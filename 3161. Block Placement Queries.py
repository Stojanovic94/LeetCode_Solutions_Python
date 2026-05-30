from sortedcontainers import SortedDict

class Obstacle:
    def __init__(self, x: int, max_gap: int, previous: Obstacle):
        self.x = x
        self.max_gap = max_gap
        self.previous = previous
        self.next = None   

    def deep_print(self):
        if self.next is not None:
            print(f"[{self.x}:{self.max_gap}] ->", end = " ")
            self.next.deep_print()
        else:
            print(f"[{self.x}:{self.max_gap}]")

    def remove(self):
        self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous
        return self.next

class Solution:
    def can_place(self, obstacles_tree: SortedDict, obstacles_max_gaps: SortedDict, x: int, size: int) -> bool:
        previous_obstacle_max_gap = obstacles_max_gaps.get(next(obstacles_max_gaps.irange(maximum=x, reverse=True), None))
        if previous_obstacle_max_gap.max_gap >= size:
            return True
        previous_obstacle = obstacles_tree.get(next(obstacles_tree.irange(maximum=x, reverse=True), None))
        if x - previous_obstacle.x >= size:
            return True
        return False

    def remove(self, obstacle_treemap: SortedDict, obstacles_max_gaps: SortedDict, x: int):
        obstacle_to_remove = obstacle_treemap.pop(x)
        next_obstacle = obstacle_to_remove.remove() # nullable
        obstacle_max_gap_to_remove = obstacles_max_gaps.pop(x, None)
        if obstacle_max_gap_to_remove is not None:
            obstacle_max_gap_to_remove.remove()
        if next_obstacle is not None:
            new_gap = next_obstacle.x - next_obstacle.previous.x
            gap_x = next_obstacle.x
            previous_obstacle_max_gap = obstacles_max_gaps.get(next(obstacles_max_gaps.irange(maximum=x, reverse=True), None))
            if previous_obstacle_max_gap.max_gap < new_gap:
                next_obstacle_max_gap = previous_obstacle_max_gap.next
                while next_obstacle_max_gap is not None and next_obstacle_max_gap.max_gap <= new_gap:
                    obstacles_max_gaps.pop(next_obstacle_max_gap.x)
                    next_obstacle_max_gap = next_obstacle_max_gap.remove()
                previous_node = previous_obstacle_max_gap
                next_node = next_obstacle_max_gap # nullable
                new_node = Obstacle(gap_x, new_gap, previous_node)
                previous_node.next = new_node
                new_node.next = next_node
                if next_node is not None:
                    next_node.previous = new_node
                obstacles_max_gaps[new_node.x] = new_node
            

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = []
        for query in queries:
            if query[0] == 1:
                obstacles.append(query[1])
        obstacles.sort()
        max_gap = 0
        first_obstacle = Obstacle(0,0,None)
        last_obstacle = first_obstacle
        first_max_gap_obstacle = Obstacle(0,0,None)
        last_max_gap_obstacle = first_max_gap_obstacle
        obstacles_max_gaps = SortedDict()
        obstacles_tree = SortedDict()
        obstacles_max_gaps[first_max_gap_obstacle.x] = first_max_gap_obstacle
        obstacles_tree[first_obstacle.x] = first_obstacle
        for i in range(0, len(obstacles)):
            gap = obstacles[i] - last_obstacle.x
            if gap > max_gap:
                max_gap = gap
                new_max_gap_obstacle = Obstacle(obstacles[i], max_gap, last_max_gap_obstacle)
                obstacles_max_gaps[new_max_gap_obstacle.x] = new_max_gap_obstacle
                last_max_gap_obstacle.next = new_max_gap_obstacle
                last_max_gap_obstacle = new_max_gap_obstacle
            new_obstacle = Obstacle(obstacles[i], max_gap, last_obstacle)
            obstacles_tree[new_obstacle.x] = new_obstacle
            last_obstacle.next = new_obstacle
            last_obstacle = new_obstacle

        first_obstacle.deep_print()
        first_max_gap_obstacle.deep_print()

        result = []
        for query in reversed(queries):
            if query[0] == 1:
                self.remove(obstacles_tree, obstacles_max_gaps, query[1])
            else:
                can_place_r = self.can_place(obstacles_tree, obstacles_max_gaps, query[1], query[2])
                result.append(can_place_r)
        result.reverse()
        return result