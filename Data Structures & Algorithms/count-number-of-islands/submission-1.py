class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0


        def bfs(r,c):
            # main data structure to implement bfs
            q = deque()

            # need to change this to 0 as corresponding bfs on neigbouring 
            # elements won't create a infinite loop i.e already been visited
            grid[r][c] = "0" 

            q.append((r,c))
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row + dr, col + dc
                    # cancelling out all the possibilites where either
                    # loop would break or don't need to add to queue
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS 
                    or grid[nr][nc] == '0'):
                        continue
                    # if its a 1, then we add to queue
                    if grid[nr][nc] == '1':
                        q.append((nr,nc))
                        # need to change this to 0 as corresponding bfs on neigbouring 
                        # elements won't create a infinite loop i.e already been visited
                        grid[nr][nc] = '0'

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r,c)
                    # say we hit a patch of 1's, Bfs takes care of this
                    # by making surrounding 1's into 0's so that its not 
                    # counted in the next iteration of this loop
                    islands += 1
        return islands
        