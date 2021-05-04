from copy import deepcopy


def rotate_table(board):
    res = list(map(list, zip(*board[::-1])))
    return res


def checkboard(cb, key, x, y):
    for i in range(m):
        for j in range(m):
            cb[y+i][x+j] += key[i][j]
    for i in range(lock_start, lock_end + 1):
        for j in range(lock_start, lock_end + 1):
            if cb[i][j] != 1:
                return False
    return True


def solution(key, lock):
    global n, m, lock_start, lock_end
    n = len(lock)
    m = len(key)
    chk_len = n + (m - 1) * 2
    chk_table = [[0 for _ in range(chk_len)] for _ in range(chk_len)]
    lock_start = m - 1
    lock_end = chk_len - m
    for i in range(n):
        for j in range(n):
            chk_table[i+m-1][j+m-1] = lock[i][j]
    rotation = 0
    while rotation != 4:
        for y in range(lock_end + 1):
            for x in range(lock_end + 1):
                tmp_table = deepcopy(chk_table)
                if checkboard(tmp_table, key, x, y):
                    return True
        key = rotate_table(key)
        rotation += 1
    return False