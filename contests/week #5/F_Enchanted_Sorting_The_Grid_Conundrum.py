# do a selection sort typa (just find the ^) on the matrix rows if you find a swappable element the store the 2 index
# then swap that index for the whole matrix and check if they are all increasing



tests = int(input())
for _ in range(tests):
    
    grid = []
    n, m = map(int, input().split())
    
    for row in range(n):
        grid.append(list(map(int, input().split())))


    unsorted_row = None
    for row in range(n):
        for col in range(1, m):
            if grid[row][col - 1] > grid[row][col]:
                unsorted_row = grid[row]
                break
        
        if unsorted_row != None:
            break
    

    if unsorted_row == None:
        print(1, 1)
        continue
    

    sorted_version = sorted(unsorted_row)
    disordered_columns = []
    can_be_good = True

    for indx in range(m):
        if unsorted_row[indx] != sorted_version[indx]:
            disordered_columns.append(indx)

            if len(disordered_columns) >= 3:
                can_be_good = False
                break
        
    if not can_be_good:
        print(-1)
        continue

    for row in range(n):
        col1, col2 = disordered_columns
        grid[row][col1], grid[row][col2] = grid[row][col2], grid[row][col1]

    for row in range(n):
        for col in range(1, m):
            if grid[row][col - 1] > grid[row][col]:
                can_be_good = False
                break
        
        if not can_be_good:
            break
    
    if not can_be_good:
        print(-1)
    
    else:
        print(disordered_columns[0] + 1, disordered_columns[1] + 1)