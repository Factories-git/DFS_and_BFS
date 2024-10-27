import sys
from collections import deque

input = sys.stdin.readline

def dfs(g,start):
    global c
    visit.add(start)
    for node in g[start]:
        if node not in visit:
            dfs(g, node)
            c += 1
    return c

c = int(input())
c1 = int(input())
g = [[] for _ in range(c)]

for i in range(c1):
    u,v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
c = 0
visit = set()
print(dfs(g, 0))