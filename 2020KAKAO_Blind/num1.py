
def solution(s):
    answer = 1001
    half = len(s) // 2 + 1
    N = len(s)
    for i in range(1, half):
        stack = []
        res = ''
        for j in range(0, N, i):
            if j + i >= N:
                substring = s[j:N]
                if stack and stack[-1] == substring:
                    stack.append(substring)
                    res += str(len(stack)) + stack[-1]
                    stack.clear()
                elif stack and stack[-1] != substring:
                    if len(stack) == 1:
                        res += stack[0]
                    else:
                        res += str(len(stack)) + stack[-1]
                    res += substring
                    stack.clear()
                elif not stack:
                    res += substring
                break
            substring = s[j:j+i]
            if not stack or stack[-1] == substring:
                stack.append(substring)
            elif stack and stack[-1] != substring:
                if len(stack) == 1:
                    res += stack[0]
                else:
                    res += str(len(stack)) + stack[-1]
                stack.clear()
                stack.append(substring)
        #print(res)
        answer = min(answer, len(res))
    return answer


s = "a"
print(solution(s))