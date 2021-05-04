from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    volunteer = defaultdict(list)
    for i in info:
        arr = list(i.split())
        pre_condition = arr[:-1]
        score = int(arr[-1])
        for j in range(5):
            combs = list(combinations([0, 1, 2, 3], j))
            for comb in combs:
                tmp = pre_condition.copy()
                for k in comb:
                    tmp[k] = '-'
                precons = '/'.join(tmp)
                volunteer[precons].append(score)

    for key in volunteer.keys():
        volunteer[key].sort()

    for q in query:
        tmp = list(q.split())
        arr = []
        for t in tmp:
            if t != "and":
                arr.append(t)
        q_precon = '/'.join(arr[:-1])
        q_score = int(arr[-1])

        res = 0
        if q_precon in volunteer:
            res = len(volunteer[q_precon]) - bisect_left(volunteer[q_precon], q_score, 0, len(volunteer[q_precon]))
        answer.append(res)
    return answer