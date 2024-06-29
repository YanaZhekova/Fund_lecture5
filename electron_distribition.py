electrons = int(input())
shells_electrons = list()

for i in range(1, electrons + 1):
    full_shells = 2 * pow(i, 2)
    if sum(shells_electrons) + full_shells == electrons:
        shells_electrons.append(full_shells)
        break
    elif sum(shells_electrons) + full_shells > electrons:
        if electrons -sum(shells_electrons)<full_shells:
            shells_electrons.append(electrons - sum(shells_electrons))
        else:
            shells_electrons.append(sum(shells_electrons) + full_shells - electrons)
        break
    else:
        shells_electrons.append(full_shells)

print(shells_electrons)
