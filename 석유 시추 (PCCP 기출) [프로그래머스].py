import sys
dic = {}
sys.setrecursionlimit(10**6)

def solution(land):
    def dfs(g, x, y, visits):
        global dic
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        count = 1
        if x <= -1 or x >= len(g) or y <= -1 or y >= len(g[0]):
            return [0, visits]
        if g[x][y] == 1:
            visits.append((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in visit:
                    visit.add((nx, ny))
                    dfs_r = dfs(g, nx, ny, visits)
                    count += dfs_r[0]
        return [count if g[x][y] == 1 else 0, visits]

    ans_c = -1
    for i in range(len(land[0])):
        c = 0
        visit = set()
        for j in range(len(land)):
            if land[j][i] == 1:
                dfs_re = dfs(land, j, i, [])
                c += dfs_re[0] - 1
                if dfs_re[0] == 0 and not (j, i) in visit:
                    c += 1
                visit.add((j, i))
                print(dfs_re)
        ans_c = max(c, ans_c)
    return ans_c

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))