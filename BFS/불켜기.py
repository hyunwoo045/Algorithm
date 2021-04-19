import sys
from collections import defaultdict, deque
input = sys.stdin.readline
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs():
    res = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0))
    while q:
        cy, cx = q.popleft()
        if (cy, cx) in graph.keys():
            while graph[(cy, cx)]:
                ly, lx = graph[(cy, cx)].pop()
                if board[ly][lx] == 0:
                    res += 1
                board[ly][lx] = 1
        for my, mx in movement:
            ny, nx = cy + my, cx + mx
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
    return res


N, M = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1
graph = defaultdict(list)
answer = 1
for _ in range(M):
    x, y, a, b = map(int, input().split())
    graph[(x-1, y-1)].append((a-1, b-1))

while True:
    turned_on = bfs()
    #print(turned_on)
    if turned_on == 0:
        break
    else:
        answer += turned_on

print(answer)