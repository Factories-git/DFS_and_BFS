from collections import deque


def bfs(land, search):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    n = len(land)
    m = len(land[0])
    queue = deque()
    visit = [[False] * m for _ in range(n)]
    visit[0][search] = True
    queue.append((0, search))  # x, y, 석유량
    maps = 1 if land[0][search] == 1 else 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if land[nx][ny] == 1:
                if dx[i] != 1 and land[x][y] == 0:
                    continue
                queue.append((nx, ny))
                maps += 1
                visit[nx][ny] = True
            if land[nx][ny] == 0 and ny == search:
                queue.append((nx, ny))
                visit[nx][ny] = True

    return maps


def solution(land):
    answer = 0
    for i in range(len(land[0])):
        answer = max(bfs(land, i), answer)
    return answer