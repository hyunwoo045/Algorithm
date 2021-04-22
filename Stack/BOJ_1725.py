import sys
input = sys.stdin.readline

N = int(input())
stack = [[int(input()), 1]]
answer = 0
for _ in range(N-1):
    cur = int(input())
    if cur == 0:
        while stack:
            answer = max(answer, stack[-1][0] * stack[-1][1])
            stack.pop()
        continue
    if not stack:
        stack.append([cur, 1])
        continue
    if cur < stack[-1][0]:
        tmp = 1
        while stack:
            if cur < stack[-1][0]:
                answer = max(answer, stack[-1][0] * stack[-1][1])
                tmp = stack[-1][1]
                stack.pop()
            else:
                break
        for i in range(len(stack)):
            stack[i][1] += 1
            answer = max(answer, stack[-1][0] * stack[-1][1])
        stack.append([cur, tmp+1])
    elif cur > stack[-1][0]:
        for i in range(len(stack)):
            stack[i][1] += 1
            answer = max(answer, stack[i][0] * stack[i][1])
        stack.append([cur, 1])
    else:
        for i in range(len(stack)):
            stack[i][1] += 1
            answer = max(answer, stack[i][0] * stack[i][1])
print(answer)