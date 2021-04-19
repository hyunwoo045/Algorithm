from collections import deque
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(sy, sx, h):
    res = 0
    visited[sy][sx] = True
    q = deque()
    q.append((sy, sx))
    cors = [(sy, sx)]
    flag = False
    while q:
        cy, cx = q.popleft()
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx]:
                    if board[ny][nx] <= h:
                        q.append((ny, nx))
                        cors.append((ny, nx))
                        visited[ny][nx] = True
            else:
                flag = True
    if flag:
        return 0
    else:
        while cors:
            co_y, co_x = cors.pop()
            board[co_y][co_x] += 1
            res += 1
        return res


N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
answer = 0
for height in range(1, 10):
    visited = [[False for _ in range(M)] for _ in range(N)]
    for y in range(1, N-1):
        for x in range(1, M-1):
            if board[y][x] == height and not visited[y][x]:
                tmp = bfs(y, x, height)
                answer += tmp
print(answer)
