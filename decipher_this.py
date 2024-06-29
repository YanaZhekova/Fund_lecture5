def find_digits(word):
    list_of_digits = list()
    for i in range(len(word)):
        if word[i].isdigit():
            list_of_digits.append(word[i])
    return list_of_digits


def replace_characters(word):
    word = list(word)
    second_char = word[1]
    last_char = word[len(word) - 1]
    for i in range(len(word)):
        if i == 1:
            word[i] = last_char
        elif i == len(word) - 1:
            word[i] = second_char
    return word


text = input().split(" ")
result = ""
for i in range(len(text)):
    first_word = text[i]
    digit_list = find_digits(first_word)
    letter_as_digit = "".join(digit_list)
    letter = chr(int(letter_as_digit))
    first_word = first_word.replace("".join(digit_list), "")
    first_word = letter + first_word
    first_word = replace_characters(first_word)
    result += "".join(first_word)
    result += " "

print(result)
