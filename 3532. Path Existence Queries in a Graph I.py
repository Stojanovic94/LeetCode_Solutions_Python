from pprint import pprint
class Solution:
    # def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    #     path_matrix = [[False] * (n) for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i, n):
    #             if i == j:
    #                 path_matrix[i][j] = True 
    #             else:
    #                 path_matrix[i][j] = path_matrix[i][j-1] and abs(nums[j-1] - nums[j]) <= maxDiff 
    #     ans = []
    #     for (q1, q2) in queries:
    #         q1, q2 = (q1,q2) if q2 > q1 else (q2, q1)
    #         ans.append(path_matrix[q1][q2])

    #     return ans


    def find_paths(self, q1, q2):
        if q2 in self.path_matrix[q1]:
            return self.path_matrix[q1][q2]
        self.path_matrix[q1][q2]  =  self.find_paths(q1, q2 -1) and (self.nums[q2] - self.nums[q2 - 1]) <= self.max_diff
        return self.path_matrix[q1][q2] 


        
    def pathExistenceQueries1(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        self.path_matrix = defaultdict(dict)
        for i in range(n):
            self.path_matrix[i][i] = True
        self.nums = nums
        self.max_diff = maxDiff
        ans = []
        for (q1, q2) in queries:
            q1, q2 = (q1,q2) if q2 > q1 else (q2, q1)
            ans.append(self.find_paths(q1, q2))
        return ans



    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        if len(nums) == 0: return []
        connected_components = [0]
        last_connected_components = 0
        for i in range(1,n):
            if nums[i]  - nums[i-1] > maxDiff:
                last_connected_components +=1
            connected_components.append(last_connected_components)

        return [connected_components[q1] == connected_components[q2] for q1, q2 in queries]

        




        