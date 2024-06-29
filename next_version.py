current_version = list(map(int, input().split(".")))


if current_version[2] == 9:
    current_version[1] = int(current_version[1]) + 1
    current_version[2] = 0
    if current_version[1] > 9:
        current_version[0] = int(current_version[0]) + 1
        current_version[1] = 0
else:
    current_version[2] = current_version[2] + 1


print(".".join(list(map(str,current_version))))