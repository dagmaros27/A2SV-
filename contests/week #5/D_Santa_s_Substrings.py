n = int(input())
arr = [input() for _ in range(n)]

arr.sort(key=lambda x: len(x))

for i in range(n - 1):
    if arr[i] not in arr[i + 1]:
        print("NO")
        break

else:
    print("YES")
    for i in arr:
        print(i)
