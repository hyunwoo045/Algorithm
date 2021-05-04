def check(result):
    for x, y, w in result:
        if w == 0:
            if y == 0 or (x-1, y, 1) in result or (x, y, 1) in result or (x, y-1, 0) in result:
                continue
            else:
                return False
        elif w == 1:
            if (x, y-1, 0) in result or (x+1, y-1, 0) in result or ((x-1, y, 1) in result and (x+1, y, 1) in result):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    res = []
    for x, y, w, h in build_frame:
        if h == 1:
            res.append((x, y, w))
            if check(res):
                continue
            else:
                for i in range(len(res)):
                    if res[i] == (x, y, w):
                        del res[i]
                        break
        elif h == 0:
            if (x, y, w) in res:
                for i in range(len(res)):
                    if res[i] == (x, y, w):
                        del res[i]
                        break
                if check(res):
                    continue
                else:
                    res.append((x, y, w))
    res = list(map(list, res))
    return sorted(res, key=lambda k: (k[0], k[1], k[2]))