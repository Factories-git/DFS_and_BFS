import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(g, start, visit):
    visit[start] = True
    for node in range(len(g)):
        if g[start][node] == 1 and not visit[node]:
            dfs(g, node, visit)


def solution(n, computers):
    c = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            dfs(computers, i, visit)
            c += 1
    return c


print(solution(	3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
