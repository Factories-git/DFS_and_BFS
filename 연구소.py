from itertools import combinations
import copy, sys

sys.setrecursionlimit(10 ** 9)


def dfs(x, y):
    global screen_shot
    if x <= -1 or x >= m or y <= -1 or y >= n or screen_shot[x][y] != 0:
        return count_safety(screen_shot)
    screen_shot[x][y] = 2
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)


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
        mx = max(dfs(x, y), mx)

    com = sorted(com)
    if com[0] == [0, 1] and com[1] == [1, 0] and com[2] == [3, 5]:
        print(count_safety(screen_shot))
        print(com)
        print('\n'.join(map(str, screen_shot)))

print(mx)

