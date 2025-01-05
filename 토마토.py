from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    visit = set()
    k = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tomato[nx][ny] == 1 or tomato[nx][ny] == -1 or (nx, ny) in visit:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                visit.add((x, y))
                queue.append((nx, ny))
    return tomato


visit = set()
m, n = map(int, input().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            re = bfs(i, j)

max_ = 1
for i in range(n):
    max_ = max(max_, max(tomato[i]))
print(max_-1)