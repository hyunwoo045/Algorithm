import heapq
from sys import maxsize
from collections import defaultdict
INF = maxsize

def dijkstra(first, graph, n):
    queue = []
    dist = [INF for _ in range(n + 1)]
    dist[0], dist[first] = 0, 0
    heapq.heappush(queue, [0, first])
    while queue:
        cur_dist, cur = heapq.heappop(queue)
        if dist[cur] < cur_dist:
            continue
        for wei, adj in graph[cur]:
            distance = cur_dist + wei
            if distance < dist[adj]:
                dist[adj] = distance
                heapq.heappush(queue, [distance, adj])
    return dist


def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for start, end, weight in fares:
        graph[start].append([weight, end])
        graph[end].append([weight, start])
    both_dist = dijkstra(s, graph, n)
    answer = INF
    for i in range(1, n + 1):
        a_dist = dijkstra(i, graph, n)
        b_dist = dijkstra(i, graph, n)
        answer = min(both_dist[i] + a_dist[a] + b_dist[b], answer)
    return answer