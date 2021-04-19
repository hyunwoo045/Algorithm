'''
외판원 순회 문제
'''


import sys
input = sys.stdin.readline


def find(now, before):
    if dp[now][before]:
        return dp[now][before]

    if before == (1 << n) - 1:
        return board[now][0] if board[now][0] > 0 else sys.maxsize

    cost = sys.maxsize
    for i in range(n):
        if i != now and before & (1 << i) == 0 and board[now][i]:
            tmp = find(i, before | (1 << i))
            cost = min(cost, tmp + board[now][i])

    dp[now][before] = cost
    return cost


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(1 << n)] for _ in range(n)]
answer = sys.maxsize
print(find(0, 1))
'''
for i in range(n):
    answer = min(answer, find(i, (1 << i)))
print(answer)
'''