n = int(input())
coins = list(map(int, input().split()))
 
coins.sort()
 
smallest_sum = 1
 
for coin in coins:
    if coin > smallest_sum:
        break
    smallest_sum += coin
 
print(smallest_sum)