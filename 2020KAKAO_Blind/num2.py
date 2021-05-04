def divide(s):
    s = list(s)
    stack = []
    left, right = 0, 0
    for a in s:
        stack.append(a)
        if a == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    u = ''.join(stack)
    v = ''.join(s[len(u):])
    return u, v

def isFine(s):
    s = list(s)
    stack = []
    for a in s:
        if a == '(':
            stack.append(a)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    if len(stack) != 0:
        return False
    return True

def convert(s):
    if s == '':
        return ''
    u, v = divide(s)
    if isFine(u):
        return u + convert(v)
    tmp = '(' + convert(v) + ')'
    u = list(u)
    u.pop(0)
    u.pop()
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    return tmp + ''.join(u)

def solution(p):
    if isFine(p):
        return p
    return convert(p)