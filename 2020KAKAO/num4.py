from collections import deque

def solution(food_times, k):
    N = len(food_times)
    foods = [[food_times[i], i+1] for i in range(N)]
    foods.sort(key=lambda x:x[0])
    q = deque(foods)
    food_eaten = 0
    while q:
        food_remained = len(q)
        cur_food, idx = q.popleft()
        if cur_food == 0:
            continue
        used_time = (cur_food - food_eaten) * food_remained
        if used_time > k:
            q.appendleft([cur_food, idx])
            foods = list(q)
            foods.sort(key=lambda x: x[1])
            #print(len(foods), k, q)
            return foods[k % len(foods)][1]
        else:
            food_eaten += cur_food - food_eaten
            k -= used_time
        #print(q, used_time, k)
    return -1