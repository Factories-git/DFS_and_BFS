#미완, 몇번 굴려야 되는지까지 코딩
from collections import deque


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
goal = [0] * 2
blue_bead = [0] * 2
red_bead = [0] * 2
for i in range(n):
    for j in range(m):
        if board[i][j] == 'O':
            goal[0] = i
            goal[1] = j
        if board[i][j] == 'R':
            red_bead[0], red_bead[1] = i, j
        if board[i][j] == 'B':
            blue_bead[0], blue_bead[1] = i, j


def bfs(start):
    queue = deque()
    queue.append(start)
    graph = [[0] * m for i in range(n)]
    while queue:
        x, y, d_x, d_y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 'O':
                graph[nx][ny] = graph[x][y]
                break
            if board[nx][ny] == '#':
                continue
            if (d_x != dx[i] or d_y != dy[i]) and board[nx][ny] != '#' and graph[nx][ny] == 0:
                queue.append((nx, ny, dx[i], dy[i]))
                graph[nx][ny] = graph[x][y] + 1
                continue
            if d_x == dx[i] and d_y == dy[i]:
                graph[nx][ny] = graph[x][y]
                queue.append((nx, ny, dx[i], dy[i]))
    print('\n'.join(map(str, graph)))
    return graph[goal[0]][goal[1]]


s = bfs(red_bead + [0, 0])
print(s)