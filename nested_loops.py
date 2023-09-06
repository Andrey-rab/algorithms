# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# n = list(map(int, input().split()))
# for i in n:
#     print('*'*i)

# по числу n найти количество простых чисел p из интервала n < p < 2n. Постулат Бертрана
n = int(input())
p = 0
for i in range(n+1,n*2):
    if i % 2 == 0 and i != 2 or i == 1:
        continue
    count = 0
    for j in range(1,int(i**0.5+1)):
        if i % j == 0:
            count += 1

    if count == 1:
        p += 1
print(p)