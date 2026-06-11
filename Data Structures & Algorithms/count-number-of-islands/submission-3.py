class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid),len(grid[0])
        islands = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = '0'
            while q:
                # 1. pop leftmost entry from queue and extract its contents
                row, col = q.popleft()
                # 2. check surroundings whether it is part of island
                for dr,dc in directions:
                    #3. extract new neighbours
                    nr,nc  = dr + row, dc + col
                    #4. check if neighbours are valid i.e it is a '1'
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0'):
                        continue
                    #5. if it is a 1, continue bfs by adding it to q
                    q.append((nr,nc))
                    #6. change the value of nodes that have been added to q to 0,
                    # as to avoid repeated additions
                    grid[nr][nc] = '0'
            
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r,c)
                    islands += 1
        return islands
        