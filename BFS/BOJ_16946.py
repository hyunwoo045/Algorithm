from collections import deque
import sys
input = sys.stdin.readline
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    cnt = 1
    while q:
        cy, cx = q.pop()
        zeros[cy][cx] = group
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and not board[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    cnt += 1
    return cnt

def countMoves(sy, sx):
    candidates = set()
    for my, mx in movement:
        ny, nx = sy + my, sx + mx
        if 0 <= ny < N and 0 <= nx < M:
            if zeros[ny][nx]:
                candidates.add(zeros[ny][nx])
    cnt = 1
    for c in candidates:
        cnt += info[c]
        cnt = cnt % 10
    return cnt

N, M = map(int, input().split())
board = [list(map(int, list(str(input().rstrip('\n'))))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
zeros = [[0 for _ in range(M)] for _ in range(N)]
group = 1
info = {}
for y in range(N):
    for x in range(M):
        if not board[y][x] and not visited[y][x]:
            cnt = bfs(y, x)
            info[group] = cnt
            group += 1

answer = [[0 for _ in range(M)] for _ in range(N)]
for y in range(N):
    for x in range(M):
        if board[y][x]:
            answer[y][x] = countMoves(y, x)

for y in range(N):
    print(''.join(map(str, answer[y])))