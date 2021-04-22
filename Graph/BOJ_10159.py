import sys
input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for y in range(n):
            for x in range(n):
                if graph[y][k] and graph[k][x]:
                    graph[y][x] = 1

n = int(input())
m = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a-1][b-1] = 1
floyd_warshall()
for y in range(n):
    ans = 0
    for x in range(n):
        if not graph[y][x] and not graph[x][y] and y != x:
            ans += 1
    print(ans)