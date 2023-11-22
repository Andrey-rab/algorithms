# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# n = list(map(int, input().split()))
# for i in n:
#     print('*'*i)

# по числу n найти количество простых чисел p из интервала n < p < 2n. Постулат Бертрана
# n = int(input())
# p = 0
# for i in range(n+1,n*2):
#     if i % 2 == 0 and i != 2 or i == 1:
#         continue
#     count = 0
#     for j in range(1,int(i**0.5+1)):
#         if i % j == 0:
#             count += 1
#
#     if count == 1:
#         p += 1
# print(p)

# lst = []
# for i in range(1000, 9999):
#     count = 0
#     for j in str(i):
#         count += int(j)
#     if count == 20:
#         lst.append(i)
# print(sum(lst))

# #n = int(input())
# lst = [8, 5, 3, 1, 4, 7, 9]
# #lst = list(map(int, input().split()))
# count = 0
# for i in range(len(lst)):
#     print(i)
#     for j in range(len(lst)-1-i):
#         print('j',j,'j' )
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#             print(lst)
#             count += 1
# print(lst)
# print(count)

n = 9
m = 3
# a = (n - b)**0.5
# b = (m - a)**0.5
# for a in range(min(n, m)+1):
#     b = (m - a) ** 0.5
#     print(b, 'bbbb')
#     for b in range(min(n, m)+1):
#         a = (n - b) ** 0.5
#         print(a , 'aaaa')
#         if a ** 2 + b == n and a + b ** 2 == m:
#             print('ответ', a, b)
#             count += 1
#             break
# print(count)
# if a**2 + b == n and a + b**2 == m:
#     print(a, b)

n, m = map(int, input().split())
a = 0
for a in range(min(n,m)+1):
    b = n - a**2
    if b >= 0 and a + b**2 == m:
        count += 1
print(count)