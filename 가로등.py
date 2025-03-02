from collections import deque

l, n, k = map(int, input().split())
arr = list(map(int, input().split()))
dx = [-1, 1]

def bfs():
    queue = deque()
    streetlights = {}
    c = 0
    for i in arr:
        queue.append(i)
        streetlights[i] = 0

    while queue:
        x = queue.popleft()
        c += 1
        print(streetlights[x])
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx <= l and nx not in streetlights:
                streetlights[nx] = streetlights[x] + 1
                queue.append(nx)
        if c == k:
            return


bfs()
