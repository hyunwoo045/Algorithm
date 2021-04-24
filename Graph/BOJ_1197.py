# 최소 스패닝 트리 (기본)

from collections import defaultdict
import sys
input = sys.stdin.readline

def get_parent(num):
    if num not in graph.keys():
        return num
    else:
        return get_parent(graph[num][0])

def union_find(num1, num2):
    a = get_parent(num1)
    b = get_parent(num2)
    if a == b:
        return False
    else:
        if a < b:
            graph[b].append(a)
        else:
            graph[a].append(b)
        return True


V, E = map(int, input().split())
lines = []
graph = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, input().split())
    lines.append((A, B, C))
lines.sort(key=lambda x: x[2])
answer = 0
for s, e, w in lines:
    if union_find(s, e):
        answer += w

print(answer)