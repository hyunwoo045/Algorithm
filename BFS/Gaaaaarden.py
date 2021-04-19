from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(greens, reds):
    visited = [["*" for _ in range(M)] for _ in range(N)]
    res = 0
    q = deque()
    for green in greens:
        sy, sx = green
        visited[sy][sx] = 1
        q.append((sy, sx, 1))
    for red in reds:
        sy, sx = red
        visited[sy][sx] = -1
        q.append((sy, sx, -1))
    while q:
        cy, cx, dist = q.popleft()
        if visited[cy][cx] == 0:
            continue
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == "*" and board[ny][nx] != 0:  # not visited
                    if dist > 0:  # green case
                        visited[ny][nx] = dist + 1
                        q.append((ny, nx, dist + 1))
                    else:  # red case
                        visited[ny][nx] = dist - 1
                        q.append((ny, nx, dist - 1))
                elif visited[ny][nx] != "*" and board[ny][nx] != 0:  # visited
                    if dist > 0 and visited[ny][nx] < 0:  # green case & red ground
                        if dist + 1 + visited[ny][nx] == 0:
                            res += 1
                            visited[ny][nx] = 0
                    elif dist < 0 and visited[ny][nx] > 0:  # red case & green ground
                        if dist - 1 + visited[ny][nx] == 0:
                            res += 1
                            visited[ny][nx] = 0
                '''
                for y in range(len(visited)):
                    print(visited[y])
                print()
                '''
    return res


N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cords = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 2:
            cords.append((y, x))

#print(cords)
combs = list(combinations([i for i in range(len(cords))], G))
#print(perms)
answer = 0
for comb in combs:
    green_cords = []
    for c in comb:
        green_cords.append(cords[c])
    red_combs = list(combinations([i for i in range(len(cords)) if i not in comb], R))
    for r_comb in red_combs:
        red_cords = []
        for c in r_comb:
            red_cords.append(cords[c])
        r = bfs(green_cords, red_cords)
        answer = max(answer, r)
print(answer)
