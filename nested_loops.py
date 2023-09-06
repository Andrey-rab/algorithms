# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# n = list(map(int, input().split()))
# for i in n:
#     print('*'*i)

n = int(input())
# p = 7 % 7
# if p % p == 0
# print(p)
p = 0
for i in range(n+1,n*2+1):
    #print(p)
    count = 0
    for j in range(2,int(i**0.5+1)):
        if i % j == 0:
            count += 1
            #print('простое число: ', i, "делить на ", j)
    if count == 1:
        p += 1
print(p)