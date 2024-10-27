import sys
sys.setrecursionlimit(10**6)
from collections import deque

input = sys.stdin.readline

def dfs(g,start, visit):
    visit[start] = True
    for node in g[start]:
        if not visit[node]:
            dfs(g, node, visit)

n,m = map(int, input().split())
g = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
c = 0
visit = [False] * (n+1)
for i in range(1, n+1):
    if not visit[i]:
        dfs(g, i, visit)
        c += 1
print(c)