tests = int(input())

for _ in range(tests):
    n , k  = list(map(int, input().split()))
    
    word = input()
    
    counter = {}
    
    for i in word:
        counter[i] = counter.get(i, 0) + 1
    
    odd = 0
    
    for i in counter.values():
        if i %2 != 0:
            odd += 1
    if odd > k+1:
        print("NO")
    else:
        print("YES")
        