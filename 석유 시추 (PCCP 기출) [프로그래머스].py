#1번 코드, 정확성 모두 통과, 효율성 시간초과
import sys

sys.setrecursionlimit(10**6)

def solution(land):
    def dfs(g, x, y):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        count = 1
        if x <= -1 or x >= len(g) or y <= -1 or y >= len(g[0]):
            return 0
        if g[x][y] == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in visit:
                    visit.add((nx, ny))
                    count += dfs(g, nx, ny)
        return count if g[x][y] == 1 else 0

    ans_c = -1
    for i in range(len(land[0])):
        c = 0
        visit = set()
        for j in range(len(land)):
            if land[j][i] == 1:
                dfs_re = dfs(land, j, i) - 1
                c += dfs_re
                if dfs_re == 0 and not (j, i) in visit:
                    c += 1
                visit.add((j, i))
        ans_c = max(c, ans_c)
    return ans_c


#2번 코드, 정확성 33.3, 효율성은 시간초과 1, 나머지 모두 실패
def solution(land):
    di = {}
    def dfs(g, x, y):
        nonlocal visits
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        count = 1
        if x <= -1 or x >= len(g) or y <= -1 or y >= len(g[0]):
            return 0
        if g[x][y] == 1:
            visits.add((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in visit:
                    visit.add((nx, ny))
                    count += dfs(g, nx, ny)
        return count if g[x][y] == 1 else 0

    ans_c = -1
    for i in range(len(land[0])):
        c = 0
        visit = set()
        for j in range(len(land)):
            if land[j][i] == 1:
                visits = set()
                if (j, i) not in di:
                    dfs_re = dfs(land, j, i) - 1
                    if dfs_re == 0 and not (j, i) in visit:
                        dfs_re += 1
                    c += dfs_re
                    for k in visits:
                        di[k] = dfs_re
                    visit.add((j, i))
                elif (j, i) in di:
                    if j != 0:
                        if land[j-1][i] == 1:
                            continue
                    c += di[(j, i)]
        ans_c = max(c, ans_c)
    return ans_c

print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))