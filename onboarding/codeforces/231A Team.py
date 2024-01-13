n = int(input())

questions = []
ans = 0
for _ in range(n):
    sure = input().split().count('1')
    if sure >= 2:
        ans += 1

print(ans)