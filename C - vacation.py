n = int(input())

dp =  [[0,0,0] for _ in range(n)]
mat = []
for i in range(n):
    nums = list(map(int, input().split()))
    mat.append(nums)

for i in range(3):
    dp[0][i] = mat[0][i]

for i in range(1,n):
    dp[i][0] = mat[i][0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = mat[i][1] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = mat[i][2] + max(dp[i-1][0], dp[i-1][1])
    
print(max(dp[n-1]))
