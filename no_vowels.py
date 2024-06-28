vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text = input()
# result = list()
# for letter in text:
#     if letter not in vowels_list:
#         result.append(letter)

result = list((x for x in text if x not in vowels_list))

print("".join(result))
