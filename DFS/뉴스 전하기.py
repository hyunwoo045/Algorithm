import sys
from collections import defaultdict
input_ = sys.stdin.readline


def dfs(x):
    res = 0
    if len(graph[x]) == 0:
        return 0
    temp = []
    for nxt in graph[x]:
        temp.append(dfs(nxt))
    temp.sort(reverse=True)
    for i in range(len(temp)):
        res = max(res, temp[i] + i + 1)
    return res

N = int(input_())
graph = defaultdict(list)
info = list(map(int, input_().split()))
for i in range(1, N):
    graph[info[i]].append(i)
print(dfs(0))