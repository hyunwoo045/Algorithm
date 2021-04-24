import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(first):
    q = []
    heapq.heappush(q, [0, first])
    while q:
        cur_dist, cur = heapq.heappop(q)
        if dist[cur] < cur_dist:
            continue
        for wei, nxt in graph[cur]:
            distance = cur_dist + wei
            if distance < dist[nxt]:
                dist[nxt] = distance
                heapq.heappush(q, [distance, nxt])

V, E = map(int, input().split())
graph = defaultdict(list)
start = int(input())
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])
dist = [sys.maxsize for _ in range(V + 1)]
dist[0], dist[start] = 0, 0
dijkstra(start)
for i in range(1, V+1):
    if dist[i] >= sys.maxsize:
        print("INF")
    else:
        print(dist[i])
