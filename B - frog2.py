n,k = map(int, input().split())

nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(nums[1] - nums[0])

for i in range(2, n):
    mnm = float("inf")
    
    for j in range(max(0,i-k),i):
        mnm = min(mnm, dp[j] + abs(nums[i] - nums[j]))
    
    dp[i] = mnm
    
print(dp[-1])
