# Линейный поиск, также известный как последовательный поиск
# этот метод используется для поиска элемента в списке.
# Суть: вы должны проверять каждый элемент списка последовательно один за другим,
# пока не найдете интересующий вас элемент или пока не закончится весь список.

# Входные данные
# Программа получает на вход в одной строке элементы списка - целые числа, разделенные пробелом. Количество элементов произвольное
# И на следующей строке вводится одно число r - значение поиска
#
# Выходные данные
# Задача. реализовать линейный алгоритм поиска введенного значения r. В случае успеха - выведите порядковый номер(индекс)
# первого найденного элемента в списке при условии, что индексация начинается с единицы.
# Если данный элемент отсутствует - необходимо вывести строку ErrorValue

# Выводим все элементы
# my_list = input().split()
# r = input()
# search_list = []
# for i in range(len(my_list)):
#     if my_list[i] == r:
#         search_list.append(i + 1)
# if search_list == []:
#     print('ErrorValue')
# else:
#     print(*search_list)

my_list = input().split()
r = input()
num_search = 0
for i in range(len(my_list)):
    if my_list[i] == r:
        num_search = i+1
        break
if num_search > 0:
    print(num_search)
else:
    print('ErrorValue')