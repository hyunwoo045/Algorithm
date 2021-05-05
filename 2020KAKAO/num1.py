def solution(record):
    answer = []
    info = {}
    for r in record:
        r = r.split()
        if r[0] == 'Enter' or r[0] == 'Change':
            info[r[1]] = r[2]

    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            message = info[r[1]] + '님이 들어왔습니다.'
            answer.append(message)
        elif r[0] == 'Leave':
            message = info[r[1]] + '님이 나갔습니다.'
            answer.append(message)
    return answer