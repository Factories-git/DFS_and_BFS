import sys

sys.setrecursionlimit(10**7)

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0] * (n+1)
visit = set()
for i in range(n-1):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)


def dfs(g, start):
    global parents
    visit.add(start)
    for node in graph[start]:
        if node not in visit:
            parents[node] = start
            dfs(g, node)


dfs(graph, 1)
print(*parents[2:], sep='\n')