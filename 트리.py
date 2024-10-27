import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
visited = [False] * N
tree = [[] for _ in range(N)]
answer = 0
p = list(map(int, input().split()))

for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def dfs(node):
    global answer
    visited[node] = True
    Cnode = 0
    for i in tree[node]:
        if not visited[i] and i != deletedNode:
            Cnode += 1
            dfs(i)
    if Cnode == 0:
        answer += 1

deletedNode = int(input())

if deletedNode == root:
    print(0)
else:
    dfs(root)
    print(answer)