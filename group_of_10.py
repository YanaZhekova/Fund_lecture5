def delete_group(x, y):
    for i in y:
        for j in x:
            if i == j:
                x.remove(j)
    return x


numbers = list(map(int, input().split(", ")))
max_group = 0
if max(numbers) < 10:
    max_group = max(numbers)
else:
    max_group = round(max(numbers) / 10)
for i in range(1, max_group + 1):
    group = list(map(int, (x for x in numbers if x <= i * 10)))
    print("Group of " + str(i * 10) + "'s: " + str(group))
    numbers = delete_group(numbers, group)
