from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
n ,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, r, c = map(int, input().split())

def bfs(start):
    global graph
    visited = set()
    queue = deque()
    for x, y, num in start:
        queue.append((x, y, num))
        visited.add((x, y))
    second = 0
    for _ in range(s):
        queue = deque(sorted(queue, key=lambda x : x[2]))
        for __ in range(len(queue)):
            x, y, num = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if (nx, ny) in visited:
                    continue
                graph[nx][ny] = num
                visited.add((nx, ny))
                queue.append((nx, ny, num))


starts = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            starts.append((i, j, graph[i][j]))
bfs(starts)
print(graph[r-1][c-1])