class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        empty, x = 0, 0
        for move in moves:
            if move == '_':
                empty += 1
            elif move == 'L':
                x -= 1
            else:
                x += 1
        return -x + empty if x < 0 else x + empty
        