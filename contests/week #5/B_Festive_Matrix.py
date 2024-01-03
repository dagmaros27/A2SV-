n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

goods = 0

for i in range(n):
    goods += matrix[i][i] 
    goods += matrix[i][n - 1 - i]  

    if i == n // 2:
        goods += sum(matrix[i])  
        goods += sum(row[i] for row in matrix)  
    middle = matrix[(n-1)//2][(n-1)//2]

goods -= (middle *3)
    

print(goods)
