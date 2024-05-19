n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(nums[1] - nums[0])

for i in range(2, n):
    dp[i] = min(dp[i-1] + abs(nums[i] - nums[i-1]), dp[i-2] + abs(nums[i] - nums[i-2]))

print(dp[-1])
