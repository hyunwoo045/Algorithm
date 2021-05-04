# 다익스트라 최소 경로 구하기 (기본)

import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start):
    q = []
    res_cnt = 1
    heapq.heappush(q, [0, start])
    while q:
        cur_dist, cur = heapq.heappop(q)
        if dist[cur] < cur_dist:
            continue
        if cur in graph.keys():
            for wei, nxt in graph[cur]:
                distance = cur_dist + wei
                if dist[nxt] > distance:
                    if dist[nxt] == sys.maxsize:
                        res_cnt += 1
                    dist[nxt] = distance
                    heapq.heappush(q, [distance, nxt])
    return res_cnt

T = int(input())
for _ in range(T):
    N, D, start = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append([s, a])
    dist = [sys.maxsize for _ in range(N + 1)]
    dist[0], dist[start] = 0, 0
    cnt = dijkstra(start)
    timeSpent = 0
    for i in range(1, N + 1):
        if i == start:
            continue
        if dist[i] >= sys.maxsize:
            continue
    max_answer = 0
    for i in range(1, N + 1):
        if dist[i] != sys.maxsize:
            max_answer = max(max_answer, dist[i])
    #print(dist)
    print(cnt, max_answer)