import sys
N,M = map(int, input().split())

a = set()
for i in range(N):
    a.add(input())
    

b = set()
for j in range(M):
    b.add(input())

ans = sorted(list(a & b))
print(len(ans))
for j in ans:
    print(j)