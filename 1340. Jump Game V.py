class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        maxSteps = [1 for i in range(len(arr))]

        stack = []
        n = len(arr)

        for i in range(n + 1):
            while len(stack) > 0 and (i == n or arr[stack[-1]] < arr[i]):
                popped_indices = [stack.pop()]
                while stack and arr[stack[-1]] == arr[popped_indices[0]]:
                    popped_indices.append(stack.pop())

                for j in popped_indices:
                    if i < n and i - j <= d:
                        maxSteps[i] = max(maxSteps[i], maxSteps[j] + 1)
                    
                    if len(stack) > 0 and j - stack[-1] <= d:
                        maxSteps[stack[-1]] = max(maxSteps[stack[-1]], maxSteps[j] + 1)
            
            if i < n:
                stack.append(i)
        
        return max(maxSteps)