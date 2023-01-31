import time


class Solution1:
    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        result = 0
        visited = set()
        queue = []
        round = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                if grid[i][j] == "1":
                    result += 1
                    queue.append((i, j))
                visited.add((i, j))
                while queue:
                    step = queue[0]
                    queue = queue[1:]
                    for x, y in round:
                        x, y = x + step[0], y + step[1]
                        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
                            continue
                        if grid[x][y] == "1":
                            if (x, y) in visited or (x, y) in queue:
                                continue
                            queue.append((x, y))
                    visited.add(step)
        return result

class Solution2:
    def numIslands(self, grid):
        Parent = {}
        def add(x):
            if x not in Parent:
                Parent[x] = x
        def find(x):
            if Parent[x] != x:
                return find(Parent[x])
            else:
                return x
        def union(x, y):
            add(x)
            add(y)
            Parent[find(y)] = find(x)

        round = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    add(tuple([i, j]))
                    for x, y in round:
                        x, y = x + i, y + j
                        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
                            continue
                        if grid[x][y] == "1":
                            union(tuple([i, j]), tuple([x, y]))
        result = 0
        for x, parent in Parent.items():
            if x == parent:
                result += 1
        return result

class Solution3:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        round = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        def search(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or grid[x][y] == "0":
                return
            grid[x][y] = '0'
            for step in round:
                search(x + step[0], y + step[1])


        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    search(i, j)
        return result


if __name__ == '__main__':
    solution = Solution3()

    start = time.time()
    result = solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 1

    start = time.time()
    result = solution.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 3

    start = time.time()
    result = solution.numIslands([
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ])
    print(result, '{:.4f}'.format(time.time() - start))
    assert result == 1
