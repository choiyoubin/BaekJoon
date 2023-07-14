n = int(input())

stack = []
ans = []
flag = 0
cum = 1
for i in range(n):
    num = int(input())
    while num >= cum:
        stack.append(cum)
        ans.append("+")
        cum += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)