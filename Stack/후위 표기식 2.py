from string import ascii_uppercase
alpha_list = list(ascii_uppercase)
alpha_info = {}
N = int(input())
postfix = list(str(input()))
for i in range(N):
    alpha_info[alpha_list[i]] = int(input())
s = []
for e in postfix:
    if e.isalpha():
        s.append(e)
    elif e in ["+", "-", "*", "/"]:
        b = s.pop()
        a = s.pop()
        if b in alpha_info.keys():
            b = alpha_info[b]
        if a in alpha_info.keys():
            a = alpha_info[a]
        if e == "+":
            s.append(a+b)
        elif e == "-":
            s.append(a-b)
        elif e == "*":
            s.append(a*b)
        elif e == "/":
            s.append(a/b)
print(format(s.pop(), ".2f"))