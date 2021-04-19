import sys
input_ = sys.stdin.readline
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

'''
백트래킹 DFS
'''
def dfs(y, x, cost):
    global answer
    if (y, x) == (0, C-1):
        if cost == K:
            answer += 1
            return
    for my, mx in movement:
        ny, nx = y + my, x + mx
        if 0 <= ny < R and 0 <= nx < C:
            if visited[ny][nx] or board[ny][nx] == "T":
                continue
            visited[ny][nx] = True
            dfs(ny, nx, cost + 1)
            visited[ny][nx] = False


R, C, K = map(int, input_().split())
board = [list(str(input_().strip())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
visited[R-1][0] = True
answer = 0
dfs(R-1, 0, 1)
print(answer)
