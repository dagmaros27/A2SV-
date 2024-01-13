tests = int(input())

for _ in range(tests):
    n = int(input())
    word = input()
    arr = [i for i in word]
    counter = 0
    indexes = set()
    i =0
    while i <= n-2:
        sub = arr[i] + arr[i+1]
        if sub == "AB" and i not in indexes:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            counter += 1
            indexes.add(i)
            i -= 1
            if i < 0 :
                i += 2
                
        else:
            i += 1
    print(counter)
            
            