numbers = input().split(", ")
numbers_list = list(map(int, numbers))

even_indexes = list()

for i in range(0, len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        even_indexes.append(i)

print(even_indexes)