employees = input().split(" ")
factor = int(input())
employees_happiness = list(map(int, employees))

average = sum(employees_happiness) / len(employees)
list_happy_employees = list((x for x in employees_happiness if x >= average))

if len(list_happy_employees) >= len(employees) / 2:
    print(f"Score: {len(list_happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(list_happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
