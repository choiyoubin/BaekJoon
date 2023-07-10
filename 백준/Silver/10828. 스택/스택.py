import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    arr = input().split()
    
    if arr[0] == 'push':
        stack.append(arr[1])
    
    elif arr[0] == 'pop':
        if not stack:
            print(-1)
        else:
            ren = stack.pop()
            print(ren)
    
    elif arr[0] == 'size':
        print(len(stack))
    
    elif arr[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    
    else:
        if not stack:
            print(-1)
        else:
            a = stack.pop()
            print(a)
            stack.append(a)
        