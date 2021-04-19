import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))
trucks = trucks[::-1]
on_bridge = deque()
time_check = deque()
time = 0
while trucks or on_bridge:
    time += 1
    if on_bridge:
        if time_check[0] + W == time:
            on_bridge.popleft()
            time_check.popleft()

    if trucks:
        if sum(on_bridge) + trucks[-1] <= L:
            cur = trucks.pop()
            on_bridge.append(cur)
            time_check.append(time)
    print(trucks, on_bridge, time_check)
print(time)
