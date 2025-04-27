#미완
from collections import deque


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


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
                print('\n'.join(map(str, graph)))
                queue.append((nx, ny, dx[i], dy[i]))
                graph[nx][ny] = graph[x][y] + 1
                print()
                continue
            if d_x == dx[i] and d_y == dy[i]:
                graph[nx][ny] = graph[x][y]
                queue.append((nx, ny, dx[i], dy[i]))
            print()
    print('\n'.join(map(str,graph)))

