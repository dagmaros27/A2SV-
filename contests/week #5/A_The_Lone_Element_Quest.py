tests = int(input())

for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))
    dic = {}  #value: frequency
    
    for i in range(n):
        dic[nums[i]] = dic.get(nums[i], 0) +1
    ans = 0
    for i in dic:
        if dic[i] == 1:
            ans = i
    ans = nums.index(ans)
    print(ans+1)            