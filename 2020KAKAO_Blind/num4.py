from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    info = defaultdict(list)
    info_reverse = defaultdict(list)
    for word in words:
        info[len(word)].append(word)
        info_reverse[len(word)].append(word[::-1])

    for i in info.values():
        i.sort()
    for i in info_reverse.values():
        i.sort()

    for query in queries:
        if query[0] == "?":
            arr = info_reverse[len(query)]
            left = query[::-1].replace('?', 'a')
            right = query[::-1].replace('?', 'z')
            answer.append(bisect_right(arr, right, 0, len(arr)) - bisect_left(arr, left, 0, len(arr)))
        else:
            arr = info[len(query)]
            left = query.replace('?', 'a')
            right = query.replace('?', 'z')
            answer.append(bisect_right(arr, right, 0, len(arr)) - bisect_left(arr, left, 0, len(arr)))
    return answer