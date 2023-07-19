from collections import deque
import sys
num = int(input())


for i in range(num):
    cnt = 0
    N, M = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    while queue:
        best = max(queue)
        front = queue.popleft()
        M -= 1
        if best == front:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if M < 0:
                M = len(queue) - 1
            
    
