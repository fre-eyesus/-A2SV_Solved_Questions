class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        

        for _ in range(4): 

            if mat == target:
                return True
            
            mat = mat[::-1]

            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

            if mat == target:
                return True
        return False