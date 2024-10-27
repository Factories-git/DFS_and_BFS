from collections import deque
import sys

input = sys.stdin.readline
def bfs(g,start):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        visit.add(node)
        for edge in g[node]:
            if edge not in visit:
                q.append(edge)
                answer[edge] += 1

n,m = map(int, input().split())
answer = [0] * (n+1)

g = [[] for _ in range(n+1)]
for i in range(m):
    c1,c2 = map(int, input().split())
    g[c1].append(c2)
for i in range(n):
    visit = set()
    bfs(g,i)

max_ = max(answer)
for i in range(1,n+1):
    if max_ == answer[i]:
        print(i, end=' ')