import sys
input = sys.stdin.readline
n, c = map(int, input().strip().split())
m = int(input())
nums = []
temps = [c] * n
for _ in range(m):
    nums.append(list(map(int, input().strip().split())))
nums = sorted(nums, key=lambda x:x[1])
ans = 0
for i in range(len(nums)):
    minNum = c + 1
    for j in range(nums[i][0],nums[i][1]):
        minNum = min(temps[j], minNum)
    t = min(minNum,nums[i][2])
    ans += t
    for j in range(nums[i][0], nums[i][1]):
        temps[j] -= t
print(ans)