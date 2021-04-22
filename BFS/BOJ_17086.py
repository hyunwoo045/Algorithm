from collections import deque
import sys
input = sys.stdin.readline
movement = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

R, C = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(R)]
cor = []
q = deque()
visited = [[-1 for _ in range(C)] for _ in range(R)]
for y in range(R):
    for x in range(C):
        if board[y][x] == 1:
            q.append((y, x, 0))
            visited[y][x] = 0

answer = 0
while q:
    cy, cx, dist = q.popleft()
    for my, mx in movement:
        ny, nx = cy + my, cx + mx
        if 0 <= ny < R and 0 <= nx < C:
            if visited[ny][nx] == -1:
                answer = max(answer, dist + 1)
                visited[ny][nx] = dist + 1
                q.append((ny, nx, dist + 1))

print(answer)
