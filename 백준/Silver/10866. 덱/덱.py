from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

queue = deque()

for i in range(n):
    arr = input().split()
    
    if arr[0] == 'push_front':
        queue.appendleft(arr[1])
    
    elif arr[0] == 'push_back':
        queue.append(arr[1])
        
    elif arr[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
             print(queue.popleft())
    
    elif arr[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    
    elif arr[0] == 'size':
        print(len(queue))
    
    elif arr[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    
    elif arr[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    else: 
        if not queue:
            print(-1)
        else:
            print(queue[-1])