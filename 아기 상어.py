from collections import deque
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
shark_size = 2
shark_x, shark_y = 0, 0

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            shark_x = i
            shark_y = j
            maps[i][j] = 0
            break

def bfs():
    distance = [[-1] * n for _ in range(n)]
    queue = deque()
    distance[shark_x][shark_y] = 0
    queue.append((shark_x, shark_y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if distance[nx][ny] != -1 or maps[nx][ny] > shark_size:
                continue
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))
    return distance


def find_fishes(dist):
    new_shark_x, new_shark_y = -1, -1
    min_distance = float('inf')
    for x in range(n):
        for y in range(n):
            if maps[x][y] != 0 and maps[x][y] < shark_size and min_distance > dist[x][y] != -1:
                new_shark_x = x
                new_shark_y = y
                min_distance = dist[x][y]
    if min_distance == float('inf'):
        return None
    else:
        return new_shark_x, new_shark_y, min_distance


ate_count = 0
re = 0
while True:
    val = find_fishes(bfs())
    if val is None:
        print(re)
        break
    shark_x = val[0]
    shark_y = val[1]
    re += val[2]
    ate_count += 1
    maps[val[0]][val[1]] = 0
    if ate_count == shark_size:
        shark_size += 1
        ate_count = 0
