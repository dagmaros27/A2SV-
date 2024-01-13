tests = int(input())

for _ in range(tests):
    n = int(input())
    arr = input().split()
    nums = [int(i) for i in arr]
    i = 0

    while i < n - 1:
        for j in range(i + 1, n):
            if (nums[i] + nums[j]) % 2 == 0:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
        i += 1

    print(*nums)
