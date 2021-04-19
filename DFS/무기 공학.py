import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(y, x, p):
    global answer
    if x == M:
        x = 0
        y += 1
    if y == N:
        answer = max(answer, p)
        return
    if not visited[y][x]:
        # right_down case
        if y+1 < N and x+1 < M and not visited[y-1][x] and not visited[y][x+1]:
            visited[y][x] = True
            visited[y+1][x] = True
            visited[y][x+1] = True
            nxt_p = p + board[y][x+1] + board[y+1][x] + (2 * board[y][x])
            dfs(y, x+1, nxt_p)
            visited[y][x] = False
            visited[y+1][x] = False
            visited[y][x+1] = False
        # right_up case
        if 0 <= y-1 and x+1 < M and not visited[y-1][x] and not visited[y][x+1]:
            visited[y][x] = True
            visited[y-1][x] = True
            visited[y][x+1] = True
            nxt_p = p + board[y][x+1] + board[y-1][x] + (2 * board[y][x])
            dfs(y, x+1, nxt_p)
            visited[y][x] = False
            visited[y-1][x] = False
            visited[y][x+1] = False
        # left_down case
        if 0 <= x-1 and y+1 < N and not visited[y+1][x] and not visited[y][x-1]:
            visited[y][x] = True
            visited[y+1][x] = True
            visited[y][x-1] = True
            nxt_p = p + board[y][x-1] + board[y+1][x] + (2 * board[y][x])
            dfs(y, x+1, nxt_p)
            visited[y][x] = False
            visited[y+1][x] = False
            visited[y][x-1] = False
        # left_up case
        if 0 <= y-1 and 0 <= x-1 and not visited[y-1][x] and not visited[y][x-1]:
            visited[y][x] = True
            visited[y-1][x] = True
            visited[y][x-1] = True
            nxt_p = p + board[y][x-1] + board[y-1][x] + (2 * board[y][x])
            dfs(y, x+1, nxt_p)
            visited[y][x] = False
            visited[y-1][x] = False
            visited[y][x-1] = False
    dfs(y, x+1, p)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0
dfs(0, 0, 0)
print(answer)