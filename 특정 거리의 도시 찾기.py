from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    ans = [0] * (n + 1)
    queue = deque()
    visit = set()
    queue.append(start)
    visit.add(start)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visit:
                ans[i] = ans[node] + 1
                queue.append(i)
                visit.add(i)
    return ans


re = bfs(x)
result = []
for idx, i in enumerate(re):
    if i == k:
        result.append(str(idx))
if result:
    print('\n'.join(result))
else:
    print(-1)
