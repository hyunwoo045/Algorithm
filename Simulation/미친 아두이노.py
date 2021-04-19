from collections import deque
import sys
input = sys.stdin.readline
movement = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]


def bfs(sy, sx):
    dist[sy][sx] = 0
    q = deque()
    q.append((sy, sx))
    while q:
        cy, cx = q.popleft()
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < R and 0 <= nx < C:
                if dist[ny][nx] == -1:
                    dist[ny][nx] = abs(sy - ny) + abs(sx - nx)
                    q.append((ny, nx))


R, C = map(int, input().split())
board = [list(str(input())) for _ in range(R)]
mad_robot = []
JS = (0, 0)
for y in range(R):
    for x in range(C):
        if board[y][x] == "R":
            mad_robot.append((y, x))
        elif board[y][x] == "I":
            Jy, Jx = y, x
commands = list(str(input()))
commands.pop()
flag = False
moved = 1

for cur_turn in commands:
    Jmy, Jmx = movement[int(cur_turn) - 1]
    board[Jy][Jx] = "."
    Jy, Jx = Jy + Jmy, Jx + Jmx
    if board[Jy][Jx] == "R":
        flag = True
        break
    board[Jy][Jx] = "I"
    dist = [[-1 for _ in range(C)] for _ in range(R)]
    bfs(Jy, Jx)
    bust_robot = []

    new_board = [["." for _ in range(C)] for _ in range(R)]
    new_board[Jy][Jx] = "I"
    for i in range(len(mad_robot)):
        mad_y, mad_x = mad_robot[i]
        closest = sys.maxsize
        closest_y, closest_x = 0, 0
        for my, mx in movement:
            if (my, mx) == (0, 0):
                continue
            mad_nxt_y, mad_nxt_x = mad_y + my, mad_x + mx
            if 0 <= mad_nxt_y < R and 0 <= mad_nxt_x < C:
                if closest > dist[mad_nxt_y][mad_nxt_x]:
                    closest = dist[mad_nxt_y][mad_nxt_x]
                    closest_y = mad_nxt_y
                    closest_x = mad_nxt_x
        board[mad_y][mad_x] = "."
        if new_board[closest_y][closest_x] == ".":
            new_board[closest_y][closest_x] = "R"
        elif new_board[closest_y][closest_x] == "R":
            if (closest_y, closest_x) not in bust_robot:
                bust_robot.append((closest_y, closest_x))
        elif board[closest_y][closest_x] == "I":
            flag = True
        mad_robot[i] = (closest_y, closest_x)

    for cor in bust_robot:
        while cor in mad_robot:
            del mad_robot[mad_robot.index(cor)]
        y, x = cor
        new_board[y][x] = "."

    if flag:
        break
    moved += 1
    board = new_board

if flag:
    print("kraj", moved)
else:
    for y in range(R):
        print(''.join(board[y]))
