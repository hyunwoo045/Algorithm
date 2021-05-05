def solution(N, stages):
    answer = []
    visited = [0 for _ in range(N + 1)]
    player_on_stage = [0 for _ in range(N + 1)]
    for s in stages:
        if s > N:
            for i in range(1, len(visited)):
                visited[i] += 1
            continue
        player_on_stage[s] += 1
        for i in range(1, s + 1):
            visited[i] += 1

    for i in range(1, N + 1):
        if visited[i] == 0:
            answer.append((0, i))
        else:
            answer.append((player_on_stage[i] / visited[i], i))
    answer.sort(key=lambda x: x[0], reverse=True)
    res = list(list(zip(*answer))[1])
    return res