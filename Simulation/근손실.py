from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = list(map(int, input().split()))

perms = list(permutations(l, N))
cur = 500
res = 0
for perm in perms:
    flag = True
    for p in perm:
        cur += p
        cur -= K
        if cur < 500:
            flag = False
            break
    if flag:
        res += 1
    cur = 500
print(res)