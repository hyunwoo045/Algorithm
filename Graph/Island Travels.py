from collections import deque
import sys
input = sys.stdin.readline
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(sy, sx, num):
    q = deque()
    q.append([sy, sx])
    visited[sy][sx] = num
    while q:
        cy, cx = q.popleft()
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < r and 0 <= nx < c:
                if visited[ny][nx] == -1 and board[ny][nx] == "X":
                    visited[ny][nx] = num
                    q.append([ny, nx])


def bfs_calCost(sy, sx, num):
    v = [[-1 for _ in range(c)] for _ in range(r)]
    v[sy][sx] = 0
    q = deque()
    q.append([sy, sx, 0])
    while q:
        cy, cx, cost = q.popleft()
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < r and 0 <= nx < c:
                if board[ny][nx] == "X":
                    if v[ny][nx] == -1 or v[ny][nx] > cost:
                        v[ny][nx] = cost
                        q.append([ny, nx, cost])
                        if path[num][visited[ny][nx]] > cost:
                            path[num][visited[ny][nx]] = cost
                if board[ny][nx] == "S":
                    if v[ny][nx] == -1 or v[ny][nx] > cost + 1:
                        v[ny][nx] = cost + 1
                        q.append([ny, nx, cost+1])
    #print("NUM", num)
    #for y in range(len(v)):
    #    print(v[y])


def find(now, before):
    if dp[now][before]:
        return dp[now][before]

    if before == (1 << island_number) - 1:
        return 0

    cost = sys.maxsize
    for i in range(island_number):
        if i != now and before & (1 << i) == 0 and path[now][i]:
            tmp = find(i, before | (1 << i))
            cost = min(cost, tmp + path[now][i])

    dp[now][before] = cost
    return cost


r, c = map(int, input().split())
board = [list(str(input())) for _ in range(r)]
#for y in range(r):
#    print(board[y])
#print()
'''
섬 그룹화하기
'''
island_number = 0
visited = [[-1 for _ in range(c)] for _ in range(r)]
for y in range(r):
    for x in range(c):
        if board[y][x] == "X" and visited[y][x] == -1:
            bfs(y, x, island_number)
            island_number += 1

#print("visited")
#for y in range(len(visited)):
#    print(visited[y])
#print()
'''
섬 간 비용 구하기
'''
path = [[sys.maxsize for _ in range(island_number)] for _ in range(island_number)]
for y in range(r):
    for x in range(c):
        if visited[y][x] != -1:
            bfs_calCost(y, x, visited[y][x])

#print("Path")
#for y in range(len(path)):
#    print(path[y])
'''
외판원 순회 알고리즘을 이용하여 최소 경로 구하기
'''
dp = [[0] * (1 << island_number) for _ in range(island_number)]
answer = sys.maxsize
for i in range(island_number):
    answer = min(answer, find(i, (1 << i)))
print(answer)
