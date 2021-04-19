exp = list(str(input()))

s = []

for e in exp:
    if "A" <= e <= "Z":
        print(e, end='')
    elif e in ["+", "-"]:
        while s and s[-1] != "(":
            print(s.pop(), end='')
        s.append(e)
    elif e in ["*", "/"]:
        while s and s[-1] in ["*", "/"]:
            print(s.pop(), end='')
        s.append(e)
    elif e == "(":
        s.append(e)
    elif e == ")":
        while s and s[-1] != "(":
            print(s.pop(), end='')
        s.pop()

while s:
    print(s.pop(), end='')
