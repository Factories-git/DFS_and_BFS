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
    visit = set()
    blue_x, blue_y = blue_bead[0], blue_bead[1]
    flag = True
    blue_flag = False
    while queue:
        x, y, d_x, d_y = queue.popleft()
        visit.add((x, y))
        for i in range(4):
            blue_donot_move = False
            red_x = x + dx[i]
            red_y = y + dy[i]
            n_blue_x = blue_x + dx[i]
            n_blue_y = blue_y + dy[i]
            if red_x < 0 or red_x >= n or red_y < 0 or red_y >= m:
                continue
            if n_blue_x < 0 or n_blue_x >= n or n_blue_y < 0 or n_blue_y >= m:
                blue_donot_move = True
                print(dx[i], dy[i], 1)
            if board[red_x][red_y] == '#':
                continue
            if board[n_blue_x][n_blue_y] == '#':
                blue_donot_move = True
                print(dx[i], dy[i], 2)
            if (red_x, red_y) in visit:
                continue
            if board[blue_x][blue_y] == '0':
                blue_flag = True
            if (d_x != dx[i] or d_y != dy[i]) and graph[red_x][red_y] == 0:
                if flag:
                    queue.append((red_x, red_y, dx[i], dy[i]))
                    graph[red_x][red_y] = graph[x][y] + 1
                elif not flag and not blue_flag:
                    return (graph[goal[0]][goal[1]], 1)
                elif blue_flag:
                    return -1
            if d_x == dx[i] and d_y == dy[i]:
                queue.append((red_x, red_y, d_x, d_y))
                graph[red_x][red_y] = graph[x][y]
                if not blue_donot_move:
                    blue_x += dx[i]
                    blue_y += dy[i]
            if board[red_x][red_y] == 'O':
                flag = False
            print(blue_x, blue_y, dx[i], dy[i])

    if not flag and not blue_flag:
        print(blue_flag, flag)
        return graph[goal[0]][goal[1]]
    if blue_flag:
        return -1

s = bfs(red_bead + [0, 0])
print(s)