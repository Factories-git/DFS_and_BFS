def dfs(y,x):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 1
    if tomato[y][x] == 1:
        tomato[y][x] = -1
        if y-1 > -1:
            dfs(y-1, x)
        if y+1 < m:
            dfs(y+1, x)
        if x-1 > -1:
            dfs(y, x-1)
        if x+1 < n:
            dfs(y, x+1)
        return True
    return False


c = 0
m,n = map(int, input().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int, input().split())))
for y in range(n):
    for x in range(m):
        if dfs(y,x):
            c += 1
print(c)