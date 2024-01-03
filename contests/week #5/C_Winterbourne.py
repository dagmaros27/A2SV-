tests = int(input())

for _ in range(tests):
    n,m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    if n > m:
        print("NO")   
    else:
        # nums.sort()
        # empty = nums[0]*2 + 1
        
        # for i in range(1, len(nums)-1):
        #     empty +=  ((2*nums[i]) - nums[i-1] + 1)
        
        # empty += (nums[-1] - nums[-2]) + (nums[-1]- nums[0]) +1
        
        empty = sum(nums) - min(nums) + n
        print(empty)

        if empty > m:
            print("NO")
        else:
            print("YES")
            
 