from itertools import combinations
def solution(orders, course):
    answer = []
    info = {}
    for c in course:
        info[c] = {}
    for order in orders:
        order = list(order)

        for c in course:
            combs = list(combinations(sorted(order), c))
            for comb in combs:
                if comb not in info[c].keys():
                    info[c][comb] = 1
                else:
                    info[c][comb] += 1

    for c in course:
        res = sorted(info[c].items(), key=lambda x:x[1], reverse=True)
        if not res:
            continue
        max_ = res[0][1]
        if max_ <= 1:
            continue
        answer.append(''.join(res[0][0]))
        for i in range(1, len(res)):
            if res[i][1] == max_:
                answer.append(''.join((res[i][0])))
            else:
                break
    return sorted(answer)