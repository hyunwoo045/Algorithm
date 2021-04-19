import heapq
import sys
input = sys.stdin.readline


def dijkstra(first):
    queue = []
    heapq.heappush(queue, [0, first])
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if cur_node in graph.keys():
            for cost, adj in graph[cur_node]:
                #print(adj, cost)
                if dist[adj][k-1] > cur_dist + cost:
                    dist[adj][k-1] = cur_dist + cost
                    dist[adj].sort()
                    heapq.heappush(queue, (cur_dist + cost, adj))


n, m, k = map(int, input().split())
graph = {}
for _ in range(m):
    s, e, w = map(int, input().split())
    if s in graph.keys():
        graph[s].append([w, e])
    else:
        graph[s] = [[w, e]]
dist = [[sys.maxsize for _ in range(k)] for _ in range(n + 1)]
dist[0][0], dist[1][0] = 0, 0
dijkstra(1)
for i in range(1, n+1):
    print(dist[i][k-1] if dist[i][k-1] != sys.maxsize else -1)
