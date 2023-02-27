class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c):
            isRoot=True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        isRoot=False
                        break
            if isRoot:
                return Node(grid[r][c], True)
            n=n//2
            topLeft = dfs(n,r,c)
            topRight= dfs(n,r,c+n)
            bottomLeft= dfs(n,r+n,c)
            bottomRight= dfs(n,r+n,c+n)
            return Node(0,False,topLeft, topRight, bottomLeft, bottomRight)
        return dfs(len(grid),0,0)
            