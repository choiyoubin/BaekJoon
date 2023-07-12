k = int(input())

stack = []
sum = 0
for i in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
        
for j in stack:
    sum += j
    
print(sum)