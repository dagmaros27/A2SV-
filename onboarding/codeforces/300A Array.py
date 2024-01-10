n = int(input())
nums = list(map(int, input().split()))
zeros,pos,neg = [],[],[]


for i in  nums:
    if i > 0 :
        pos.append(i)
    elif i < 0:
        neg.append(i)
    else:
        zeros.append(i)
if len(pos) == 0:
    pos.append(neg.pop())
    pos.append(neg.pop())

if len(neg) %2 == 0:
    zeros.append(neg.pop())


print(len(neg), *neg)
print(len(pos), *pos)
print(len(zeros), *zeros)
