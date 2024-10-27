from collections import deque , defaultdict
import sys

def DFS(graph,v,dfs):
    stack = [v]
    re = []

    while stack:
        node = stack.pop()
        if not node in dfs:
            dfs.add(node)
            re.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    return re
def BFS(graph, v, bfs):
    queue = deque([v])
    re = []

    while queue:
        node = queue.popleft()
        if not node in bfs:
            bfs.add(node)
            re.append(node)
            queue.extend(sorted(graph[node]))
    return re

input = sys.stdin.readline

n,m,v = map(int, input().split())

graph = {i : [] for i in range(1,n+1)}
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs = set()
dfs = set()
dfs_re = DFS(graph,v,dfs)
bfs_re = BFS(graph,v,bfs)

print(' '.join(map(str,dfs_re)))
print(' '.join(map(str,bfs_re)))