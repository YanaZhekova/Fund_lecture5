words = input().split(" ")
palindrome = input()

palindrome_list = list((word for word in words if word == "".join(reversed(word))))
# palindrome_list = list()
#
# for word in words:
#     reversed_word = "".join(reversed(word))
#     if word == reversed_word:
#         palindrome_list.append(word)

count = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {count} times")