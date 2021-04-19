import sys
input = sys.stdin.readline
movement = [(0, 1), (0, -1), (-1, 0), (1, 0)]
opposite = [1, 0, 3, 2]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess = [[list() for _ in range(n)] for _ in range(n)]
chess_info = {}
for i in range(k):
    r, c, d = map(int, input().split())
    chess[r-1][c-1].append(i)
    chess_info[i] = [r-1, c-1, d-1]
cnt = 1
while cnt <= 1000:
    for i in range(k):
        cy, cx, cd = chess_info[i]
        #print(cy, cx, cd)
        if chess[cy][cx][0] != i:
            continue
        ny, nx = cy + movement[cd][0], cx + movement[cd][1]
        if not 0 <= ny < n or not 0 <= nx < n or board[ny][nx] == 2:
            nd = opposite[cd]
            ny, nx = cy + movement[nd][0], cx + movement[nd][1]
            chess_info[i][2] = nd
            if not 0 <= ny < n or not 0 <= nx < n or board[ny][nx] == 2:
                continue
        tmp = chess[cy][cx][:]
        chess[cy][cx] = []
        if board[ny][nx] == 1:
            tmp = tmp[::-1]
        for piece in tmp:
            chess[ny][nx].append(piece)
            chess_info[piece][0], chess_info[piece][1] = ny, nx

        #print(chess[ny][nx])

        if len(chess[ny][nx]) >= 4:
            print(cnt)
            sys.exit()
    cnt += 1
'''
        for j in range(len(chess)):
            print(chess[j])
        print()
'''
print(-1)