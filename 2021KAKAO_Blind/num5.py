h, m = 3600, 60
def time_to_second(s):
    tmp = s.split(":")
    tmp = list(map(int, tmp))
    res = (tmp[0] * h) + (tmp[1] * m) + tmp[2]
    return res

def second_to_time(n):
    res = ""
    rh, rm = divmod(n, 3600)
    rh = str(rh) if rh >= 10 else "0"+str(rh)
    res += rh + ":"
    rm, rs = divmod(rm, 60)
    rm = str(rm) if rm >= 10 else "0"+str(rm)
    rs = str(rs) if rs >= 10 else "0"+str(rs)
    res += rm + ":" + rs
    return res

def solution(play_time, adv_time, logs):
    pt = time_to_second(play_time)
    at = time_to_second(adv_time)
    seq = [0 for _ in range(pt+1)]
    for l in logs:
        s, e = l.split("-")
        st = time_to_second(s)
        et = time_to_second(e)
        seq[st] += 1
        seq[et] -= 1

    for i in range(1, pt+1):
        seq[i] += seq[i-1]
    for i in range(1, pt+1):
        seq[i] += seq[i-1]

    max_time = 0
    max_ = seq[at]
    for i in range(pt + 1):
        et = i + at if i + at < pt else pt
        sum_played = seq[et] - seq[i]
        if max_ < sum_played:
            max_ = sum_played
            max_time = i + 1
    return second_to_time(max_time)