# Сортировка пузырьком

start_list = [5, 4, 3, 2, 1, 24, 6, 4, 5, 10, 7]
# start_list.sort()
# print(start_list)

# start_list = sorted(start_list)
# print(start_list)

for item in range(len(start_list)-1):
    for j in range(len(start_list)-1-item):
        if start_list[j] > start_list[j + 1]:
            start_list[j], start_list[j + 1] = start_list[j + 1], start_list[j]
print(start_list)

