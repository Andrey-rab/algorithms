my_list = [7, 2, 4, 8, 3, 4, 9, 1]
# Первое решение (инвертирование сортировки пузырьком)
# n = int(input())
# my_list = list(map(int, input().split()))
# for i in range(1, len(my_list)):
#     #print('DO', my_list[i], i)
#     for j in range(i, 0, -1):
#         #print(my_list[j], j)
#         if my_list[j] < my_list[j-1]:
#             my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
#             #print('es', my_list[j], j)
#         else:
#             break
# print(*my_list)

# Моё решение
for i in range(1, len(my_list)):
    element = my_list[i]
    j = i
    while j > 0 and element < my_list[j - 1]:
        my_list[j] = my_list[j - 1]
        j -= 1
    my_list[j] = element
print(my_list)

# Второй способ от чата GPT
# for i in range(1, len(my_list)):
#         element = my_list[i]  # Текущий элемент, который мы хотим вставить в отсортированную часть
#         # Перемещаем элементы больше key на одну позицию вперед
#         j = i - 1
#         while j >= 0 and element < my_list[j]:
#             my_list[j + 1] = my_list[j]
#             j -= 1
#         # Вставляем key в правильную позицию
#         my_list[j + 1] = key