from collections import deque
import sys

input = sys.stdin.readline

def bfs(g, start, need):
    q = deque()
    visit = set()
    visit.add(start)
    c = 0
    for e, w in g[start]:
        visit.add(e)
        q.append((e, w))
    while q:
        node, us = q.popleft()
        if us >= need:
            c += 1
        for edge, usado in g[node]:
            if edge not in visit:
                visit.add(node)
                q.append((edge, min(us, usado)))
    return c


n, Q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))
for i in range(Q):
    k, v = map(int, input().split())
    print(bfs(graph, v, k))