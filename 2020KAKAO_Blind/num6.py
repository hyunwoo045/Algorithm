# 원형으로 표현되는 배열이 주어지고, 반시계 방향으로도 탐색이 가능하다면
# 배열의 길이를 2배로 늘려 선형 형태로 만들어주어 탐색하기 편하게 하자.

from itertools import permutations
from sys import maxsize

def solution(n, weak, dist):
    weak_len = len(weak)
    answer = maxsize
    for i in range(weak_len):
        weak.append(weak[i] + n)

    perms = list(map(list, permutations(dist, len(dist))))
    for i in range(weak_len):
        start = [weak[j] for j in range(i, i + weak_len)]
        for perm in perms:
            res = 1
            distance = 0
            check_len = start[0] + perm[0]

            for k in range(weak_len):
                if start[k] > check_len: # 한명 더 필요
                    res += 1
                    distance += 1
                    check_len = start[k] + perm[distance]
            answer = min(answer, res)
    if answer > len(dist):
        return -1
    return answer