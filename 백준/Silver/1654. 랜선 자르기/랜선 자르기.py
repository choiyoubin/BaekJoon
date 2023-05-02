K, N = map(int, input().split())
num = [0] * K
sum = 0

for i in range(K):
    num[i] = int(input())


start = 1
end = max(num)

while (start <= end):
    mid = (start + end) // 2
    sum = 0
    for i in range(K):
        sum += num[i] // mid
    if sum >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
        
    
        
    

