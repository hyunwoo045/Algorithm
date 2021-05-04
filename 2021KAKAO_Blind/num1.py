def solution(new_id):
    # 1
    answer = new_id.lower()

    # 2
    tmp = ''
    for s in answer:
        if not s.isalnum():
            if s not in ["-", ".", "_"]:
                continue
        tmp += s
    answer = tmp

    # 3
    tmp = ''
    for s in answer:
        if tmp == '':
            tmp += s
            continue
        if tmp[-1] == '.' and s == '.':
            continue
        tmp += s
    answer = tmp

    # 4
    while answer and answer[0] == ".":
        answer = answer[1:]
    while answer and answer[-1] == ".":
        answer = answer[:len(answer) - 1]

    # 5
    if answer == '':
        answer = "a"

    # 6
    if len(answer) >= 15:
        answer = answer[:15]
    while answer[-1] == ".":
        answer = answer[:len(answer) - 1]

    # 7
    last = answer[-1]
    while len(answer) <= 2:
        answer += last

    return answer