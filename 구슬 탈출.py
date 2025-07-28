
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
    visit = set()
    visit.add(tuple(start[:-1]))
    while queue:
        red_x, red_y, blue_x, blue_y, count = queue.popleft()
        if count >= 10:
            return -1
        for i in range(4):
            flag = False
            blue_flag = False
            b_c, r_c = 0, 0
            repeat = n if dy[i] == 0 else m
            new_rx, new_ry, new_bx, new_by = red_x, red_y, blue_x, blue_y
            for j in range(repeat):
                new_rx += dx[i]
                new_ry += dy[i]
                if board[new_rx][new_ry] == '#':
                    new_rx -= dx[i]
                    new_ry -= dy[i]
                    break
                if board[new_rx][new_ry] == 'O':
                    flag = True
                    break
                r_c += 1
            for j in range(repeat):
                new_bx += dx[i]
                new_by += dy[i]
                if board[new_bx][new_by] == '#':
                    new_bx -= dx[i]
                    new_by -= dy[i]
                    break
                if board[new_bx][new_by] == 'O':
                    blue_flag = True
                    break
                b_c += 1

            if blue_flag:
                continue
            if flag:
                return count + 1

            if new_rx == new_bx and new_ry == new_by:
                if dx[i] != 0:
                    if r_c > b_c:
                        new_rx -= dx[i]
                    else:
                        new_bx -= dx[i]
                elif dy[i] != 0:
                    if r_c > b_c:
                        new_ry -= dy[i]
                    else:
                        new_by -= dy[i]

            if (new_rx, new_ry, new_bx, new_by) not in visit:
                queue.append((new_rx, new_ry, new_bx, new_by, count + 1))
                visit.add((new_rx, new_ry, new_bx, new_by))
    return -1


s = bfs(red_bead + blue_bead + [0])
print(s)