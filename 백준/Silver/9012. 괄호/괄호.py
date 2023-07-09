import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    arr = list(input().rstrip())
    
    for j in range(len(arr)):
        if arr[j] == '(':
            stack.append(arr[j])
        else:
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
    
    stack = []