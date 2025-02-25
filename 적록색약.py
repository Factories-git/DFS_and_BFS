import sys

sys.setrecursionlimit(10**6)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, color):
    global visit_
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if g[x][y] == color and (x, y) not in visit_:
        visit_.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, color)
        return True

    return False


n = int(input())
g = [list(input()) for i in range(n)]
normal = 0
red_green_color_blindness = 0
visit_ = set()
for i in range(n):
    for j in range(n):
        if dfs(i, j, g[i][j]):
            normal += 1

for i in range(n):
    for j in range(n):
        if g[i][j] == 'R':
            g[i][j] = 'G'
visit_ = set()
for i in range(n):
    for j in range(n):
        if dfs(i, j, g[i][j]):
            red_green_color_blindness += 1
print(normal, red_green_color_blindness)