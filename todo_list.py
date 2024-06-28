command = input()
todo_list = ["" for x in range(11)]

while command != "End":
    command_info = command.split("-")
    importance = int(command_info[0])
    note = command_info[1]
    todo_list[importance] = note
    command = input()

todo_list = list((x for x in todo_list if x != ""))
print(todo_list)
