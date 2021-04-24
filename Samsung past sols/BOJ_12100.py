import sys, copy
from itertools import chain
input = sys.stdin.readline

def move_up(b):
    for x in range(N):
        cur = 0
        row = 0
        for y in range(N):
            if b[y][x]:
                if cur == 0:
                    cur = b[y][x]
                else:
                    if cur == b[y][x]:
                        b[row][x] = 2 * cur
                        row += 1
                        cur = 0
                    else:
                        b[row][x] = cur
                        row += 1
                        cur = b[y][x]
            b[y][x] = 0
        if cur != 0:
            b[row][x] = cur
    return b

def move_down(b):
    for x in range(N):
        cur = 0
        row = N - 1
        for y in range(N-1, -1, -1):
            if b[y][x]:
                if cur == 0:
                    cur = b[y][x]
                else:
                    if cur == b[y][x]:
                        b[row][x] = 2 * cur
                        row -= 1
                        cur = 0
                    else:
                        b[row][x] = cur
                        row -= 1
                        cur = b[y][x]
            b[y][x] = 0
        if cur != 0:
            b[row][x] = cur
    return b

def move_left(b):
    for y in range(N):
        col = 0
        cur = 0
        for x in range(N):
            if b[y][x]:
                if cur == 0:
                    cur = b[y][x]
                else:
                    if cur == b[y][x]:
                        b[y][col] = 2 * cur
                        col += 1
                        cur = 0
                    else:
                        b[y][col] = cur
                        col += 1
                        cur = b[y][x]
            b[y][x] = 0
        if cur != 0:
            b[y][col] = cur
    return b

def move_right(b):
    for y in range(N):
        col = N - 1
        cur = 0
        for x in range(N-1, -1, -1):
            if b[y][x]:
                if cur == 0:
                    cur = b[y][x]
                else:
                    if cur == b[y][x]:
                        b[y][col] = 2 * cur
                        col -= 1
                        cur = 0
                    else:
                        b[y][col] = cur
                        col -= 1
                        cur = b[y][x]
            b[y][x] = 0
        if cur != 0:
            b[y][col] = cur
    return b

def dfs(board, cnt):
    global answer
    if cnt == 5:
        answer = max(answer, max(chain(*board)))
        return
    dfs(move_up(copy.deepcopy(board)), cnt + 1)
    dfs(move_down(copy.deepcopy(board)), cnt + 1)
    dfs(move_left(copy.deepcopy(board)), cnt + 1)
    dfs(move_right(copy.deepcopy(board)), cnt + 1)


N = int(input())
board = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
answer = 0
dfs(board, 0)
print(answer)

