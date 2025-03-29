from collections import deque

direction = [(-2, 1), (-1, 2), (1, -2), (2, -1), (-2, -1), (-1, -2), (1, 2), (2, 1)]


def bfs(start_x, start_y):
    queue = deque()
    visit = set()
    visit.add((start_x, start_y))
    queue.append((start_x, start_y, 0))
    while queue:
        x, y, dis = queue.popleft()
        if x == end_x and y == end_y:
            return dis
        for i, j in direction:
            nx, ny, ndis = x + i, y + j, dis + 1
            if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in visit:
                continue
            queue.append((nx, ny, ndis))
            visit.add((nx, ny))


t = int(input())
for _ in range(t):
    n = int(input())
    s_x, s_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(s_x, s_y))