N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
num = list(map(int, input().split()))

def bs(l, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if l[mid] == target:
        return cnt.get(target)
    elif l[mid] > target:
        return bs(l, target, start, mid-1)
    else:
        return bs(l, target, mid+1, end)

cnt = {}
for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in num:
    print(bs(arr, i, 0, len(arr)-1), end = ' ')