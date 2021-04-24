import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(cur):
    check[cur] = True
    for i in tree[cur]:
        if not check[i]:
            dfs(i)
            dp[cur][0] += dp[i][1]
            dp[cur][1] += min(dp[i])
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [[0, 1] for _ in range(N+1)]
check = [False for _ in range(N+1)]
dfs(1)
print(min(dp[1]))