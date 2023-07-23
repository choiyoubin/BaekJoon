import sys

N = int(input())
Nlist = set(map(int, sys.stdin.readline().split()))
M = int(input())
Mlist = list(map(int, sys.stdin.readline().split()))

ans = []
for i in Mlist:
    if i in Nlist:
        ans.append(1)
    else:
        ans.append(0)

for j in ans:
    print(j, end=' ')
