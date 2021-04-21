import sys
input = sys.stdin.readline

def parse(c, g, res):
    for i in range(1, N):
        if g[i - 1] != c[i - 1]:
            res += 1
            c[i - 1] = "1" if c[i - 1] == "0" else "0"
            c[i] = "1" if c[i] == "0" else "0"
            if i != N - 1:
                c[i + 1] = "1" if c[i + 1] == "0" else "0"
    if c == g:
        return res
    else:
        return -1

N = int(input())
init = str(input().strip())
goal = list(str(input().strip()))
cur = list(init)
ans = parse(cur, goal, 0)
if ans == -1:
    cur = list(init)
    cur[0] = "1" if cur[0] == "0" else "0"
    cur[1] = "1" if cur[1] == "0" else "0"
    ans = parse(cur, goal, 1)
    if ans == -1:
        print(-1)
    else:
        print(ans)
else:
    print(ans)