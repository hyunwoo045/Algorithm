import sys
from collections import deque
input = sys.stdin.readline
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(sy, sx):
    cords = []
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    cords.append([sy, sx])
    while q:
        cy, cx = q.popleft()
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < r and 0 <= nx < c:
                if board[ny][nx] == "x" and not visited[ny][nx]:
                    cords.append([ny, nx])
                    visited[ny][nx] = True
                    q.append([ny, nx])
    return cords


r, c = map(int, input().split())
board = [list(str(input())) for _ in range(r)]
for y in range(len(board)):
    board[y].pop()
n = int(input())
turn = list(map(int, input().split()))


for i in range(n):
    height = r - turn[i]
    if i % 2 == 0:  # 왼쪽에서 던짐
        for j in range(c):
            if board[height][j] == "x":
                board[height][j] = "."
                break
    else:  # 오른쪽에서 던짐
        for j in range(c-1, -1, -1):
            if board[height][j] == "x":
                board[height][j] = "."
                break
    # 바닥에 붙은 조각
    bottoms = []
    visited = [[False for _ in range(c)] for _ in range(r)]
    #for y in range(len(board)):
    #   print(''.join(board[y]))
    for j in range(c):
        if board[r-1][j] == "x" and not visited[r-1][j]:
            bottoms += (bfs(r-1, j))
    #print(bottoms)
    cluster = []
    for y in range(r):
        for x in range(c):
            if board[y][x] == "x" and not visited[y][x]:
                cluster = bfs(y, x)
                break
    if len(cluster) == 0:  # 떨어진 클러스터 없음.
        continue
    else:                  # 떨어진 클러스터가 있을 경우.
        height = 1
        for y, x in cluster:
            board[y][x] = "."
        while True:
            flag = True
            for y, x in cluster:
                if y + height >= r or board[y + height][x] == "x":
                    flag = False
            if not flag:
                break
            height += 1
        height -= 1
        for y, x in cluster:
            board[y + height][x] = "x"

for y in range(r):
    print(''.join(board[y]))
