import sys
from collections import deque
LAST = 10000 * 100
input = sys.stdin.readline
movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().rstrip('\n').split())
    board[y-1][x-1] = 1
q = deque()
q.append((0, 0))
commands = []
L = int(input())
for _ in range(L):
    a, b = map(str, input().rstrip('\n').split())
    commands.append((int(a), b))
commands = commands[::-1]
direction = 0
cnt = 1
cy, cx = 0, 0
while cnt < LAST:
    my, mx = movement[direction]
    ny, nx = cy + my, cx + mx
    if not (0 <= ny < N and 0 <= nx < N):  # 벽에 부딪힘
        print(cnt)
        sys.exit()
    elif (ny, nx) in q:  # 몸에 부딪힘
        print(cnt)
        sys.exit()
    else:
        q.append((ny, nx))
        if board[ny][nx] != 1:
            q.popleft()
        board[ny][nx] = 0
    if commands:
        if cnt == commands[-1][0]:
            if commands[-1][1] == "D":
                direction = (direction + 1) % 4
            elif commands[-1][1] == "L":
                direction = (direction - 1) % 4
            commands.pop()
    cnt += 1
    cy, cx = ny, nx