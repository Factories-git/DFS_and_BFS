from itertools import combinations
import copy, sys

sys.setrecursionlimit(10 ** 9)


def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if screen_shot[nx][ny] == 0:
                screen_shot[nx][ny] = 2
                dfs(nx, ny)

def count_safety(lab):
    return sum(row.count(0) for row in lab)


n, m = map(int, input().split())
lab = []
for i in range(n):
    lab.append(list(map(int, input().split())))
safety = [[i, j] for i in range(n) for j in range(m) if lab[i][j] == 0]
virus = [[i, j] for i in range(n) for j in range(m) if lab[i][j] == 2]
mx = 0
for com in list(combinations(safety, 3)):
    screen_shot = copy.deepcopy(lab)
    for x, y in com:
        screen_shot[x][y] = 1
    for x, y in virus:
        dfs(x, y)

    mx = max(mx, count_safety(screen_shot))
print(mx)

