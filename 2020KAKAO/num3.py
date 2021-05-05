from itertools import combinations
def solution(relation):
    R = len(relation)
    C = len(relation[0])
    combs = []
    for i in range(1, C+1):
        combs.extend(combinations([j for j in range(C)], i))
    cand = []
    for comb in combs:
        r = [tuple([item[c] for c in comb]) for item in relation]
        r = set(r)
        if len(r) == R:
            cand.append(comb)
    left, right = 0, 1
    while left < len(cand):
        if right >= len(cand):
            left += 1
            right = left + 1
            continue
        if len(set(cand[left])) == len(set(cand[left]).intersection(set(cand[right]))):
            del cand[right]
        else:
            right += 1
    return len(cand)