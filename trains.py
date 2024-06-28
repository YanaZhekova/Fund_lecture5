number_of_wagons = int(input())

wagons = [0 for i in range(number_of_wagons)]
command = input()

while command != 'End':
    command = command.split(' ')
    current_command = command[0]

    if current_command == 'add':
        people = int(command[1])
        wagons[len(wagons)-1] += people
    elif current_command == 'insert':
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif current_command == 'leave':
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people

    command = input()

print(wagons)
