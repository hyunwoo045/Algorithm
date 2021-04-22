import sys
input = sys.stdin.readline
N, M = map(int, input().split())
know_truth = list(map(int, input().split()))
if know_truth[0] == 0:
    print(M)
    sys.exit()
know_truth = set(know_truth[1:])
partyList = []
possible = [1 for _ in range(M)]
for _ in range(M):
    partyList.append(set(list(map(int, input().split()))[1:]))
for _ in range(M):
    for i in range(M):
        if know_truth.intersection(partyList[i]):
            possible[i] = 0
            know_truth = know_truth.union(partyList[i])
print(sum(possible))