import sys
input = sys.stdin.readline
movement = [(0, -1), (-1, 0), (-1, -1)]

M, N = map(int, input().split())
board = [[1 for _ in range(M)] for _ in range(M)]
fixedGrown = [0 for _ in range(2*M - 1)]
for _ in range(N):
    arr = list(map(int, input().split()))
    idx = arr[0]
    for _ in range(arr[1]):
        fixedGrown[idx] += 1
        idx += 1
    for _ in range(arr[2]):
        fixedGrown[idx] += 2
        idx += 1

cy, cx = 0, M-1
while fixedGrown:
    cur = fixedGrown.pop()
    board[cy][cx] += cur
    if cx - 1 >= 0:
        cx -= 1
    elif cx - 1 < 0:
        cy += 1

for y in range(1, M):
    for x in range(1, M):
        board[y][x] = board[0][x]

for y in range(M):
    for x in range(M):
        print(board[y][x], end=" ")
    print()