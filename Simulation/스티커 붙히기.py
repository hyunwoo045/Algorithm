import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
laptop = [[0 for _ in range(M)] for _ in range(N)]
stickers = []
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(sticker)
'''
for sticker in stickers:
    for y in range(len(sticker)):
        print(sticker[y])
    print()
'''
for sticker in stickers:
    rotation = 0
    while rotation < 4:
        for y in range(N):
            for x in range(M):

                flag = True
                for r in range(len(sticker)):
                    for c in range(len(sticker[r])):
                        if y + r < N and x + c < M:
                            if laptop[y + r][x + c] + sticker[r][c] > 1:
                                flag = False
                        else:
                            flag = False
                if flag:
                    for r in range(len(sticker)):
                        for c in range(len(sticker[r])):
                            laptop[y + r][x + c] += sticker[r][c]
                    break
            if flag:
                break
        if flag:
            break
        else:
            sticker = list(map(list, zip(*sticker[::-1])))
            rotation += 1

res = 0
for y in range(N):
    for x in range(M):
        if laptop[y][x] == 1:
            res += 1
print(res)