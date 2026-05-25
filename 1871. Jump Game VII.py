class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1' or '1' * maxJump in s:
            return False
        n = len(s)
        if minJump == maxJump:
            return (n - 1) % minJump == 0 and '1' not in s[::minJump]

        maxJump_1 = maxJump + 1
        n_maxJump_1 = n - maxJump_1
        n_minJump = n - minJump
        
        visited = set([0])
        stack = [0]
        while stack:
            i = stack.pop()
            lower = i + minJump
            for j, c in enumerate(s[lower:min(n_minJump, i + maxJump_1)], start=lower):
                if j not in visited and c == '0':
                    if j >= n_maxJump_1:
                        return True
                    stack.append(j)
                    visited.add(j)
            
        return False