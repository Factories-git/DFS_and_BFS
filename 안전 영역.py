import sys

sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, g, k):
    global visit
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if g[x][y] > k and (x, y) not in visit:
        visit.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, g, k)
        return True
    return False


max_ = 1
for i in range(101):
    c = 0
    visit = set()
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:
                dfs_re = dfs(x, y, graph, i)
                if dfs_re:
                    c += 1
    max_ = max(max_, c)
print(max_)