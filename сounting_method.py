# Метод подсчета используется для нахождения количества элементов в списке,
# при условии если вам известно в каких пределах будут значения элементов списка.
# a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
# count = [0] * 6
# for i in a:
#     count[i] += 1
# print(count)


n = list(map(int, input()))
result = [0]*(max(n)+1)
for i in n:
    result[i] += 1
print(result)
for i in range(len(result)):
    if result[i] > 0:
        print(i, result[i])