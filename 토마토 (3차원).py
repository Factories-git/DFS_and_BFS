from collections import deque

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
df = [0, 0, 0, 0, 1, -1]

def bfs(fer):
    global tomato
    visit = set()
    queue = deque()
    for f, x, y in fer:
        queue.append((f, x, y))
    while queue:
        f, x, y = queue.popleft()
        for i in range(6):
            nf, nx, ny = f + df[i], x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nf < 0 or nf >= h:
                continue
            if tomato[nf][nx][ny] == 1 or tomato[nf][nx][ny] == -1 or (nf, nx, ny) in visit:
                continue
            if tomato[nf][nx][ny] == 0:
                tomato[nf][nx][ny] = tomato[f][x][y] + 1
                visit.add((nf, nx, ny))
                queue.append((nf, nx, ny))


m, n, h = map(int, input().split())
tomato = []
ferment = []
for i in range(h):
    tomato.append([])
    for j in range(n):
        tomato[i].append(list(map(int, input().split())))
print(tomato)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                ferment.append((i, j, k))

bfs(ferment)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)

max_ = 1
for i in range(h):
    for j in range(n):
        max_ = max(max_, max(tomato[i][j]))
print(max_-1 if max_ - 1 != 0 else 0)