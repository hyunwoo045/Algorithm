import sys
input = sys.stdin.readline

def floyd_marshall():
    for k in range(N):
        for y in range(N):
            for x in range(N):
                if board[y][k] and board[k][x]:
                    board[y][x] = 1

N = int(input())
M = int(input())
board = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
plan = list(map(int, input().rstrip('\n').split()))
floyd_marshall()
flag = True
for i in range(1, M):
    a, b = plan[i-1] - 1, plan[i] - 1
    if a != b:
        if board[a][b] == 0:
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")