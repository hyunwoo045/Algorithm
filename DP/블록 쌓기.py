import sys
input_ = sys.stdin.readline

N, M, H = map(int, input_().split())
dp = [0] * (H+1)
nums = list(map(int, input_().split()))
dp[0] = 1
for num in nums:
    dp[num] += 1
for _ in range(1, N):
    nums = list(map(int, input_().split()))
    nums.append(0)
    temp = [0 for _ in range(H + 1)]
    for num in nums:
        for i in range(H+1):
            if dp[i] == 0:
                continue
            if num + i > H:
                continue
            temp[num + i] += dp[i]
    dp = temp
print(dp[H] % 10007)