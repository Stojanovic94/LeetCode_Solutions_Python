class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        st,ed=0,n-1
        while st<ed:
            for i in range(n):
                matrix[st][i],matrix[ed][i]=matrix[ed][i],matrix[st][i]
            st=st+1
            ed=ed-1
        for i in range(n):
            for j in range(i):
                 matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        