import sys

input = sys.stdin.readline

N, M = map(int, input().split())


pocketmon = {}
for i in range(1, N+1):
    name = input().rstrip()
    pocketmon[i] = name
    pocketmon[name] = i

for i in range(M):
    s = input().rstrip()
    if s.isdigit():
        print(pocketmon[int(s)])
    else:
        print(pocketmon[s])
        