from collections import deque

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
maps_new = [[0] * m for _ in range(n)]


def bfs(start):
    global maps_new
    queue = deque()
    visit = [[False] * m for _ in range(n)]
    queue.append((start[0], start[1], 0))
    visit[start[0]][start[1]] = True
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visit[nx][ny] or maps[nx][ny] == 'W':
                continue
            maps_new[nx][ny] = max(maps_new[nx][ny], dist + 1)
            queue.append((nx, ny, dist + 1))
            visit[nx][ny] = True

m_ = 0
for x in range(n):
    for y in range(m):
        if maps[x][y] == 'L':
            bfs((x, y))
for x in range(n):
    for y in range(m):
        m_ = max(m_, maps_new[x][y])
print(m_)