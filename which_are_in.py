first_list = input().split(", ")
second_list = input().split(", ")

result = list((x for x in first_list if (y for y in second_list if y.__contains__(x))))

# result = list()
# for i in first_list:
#     for j in second_list:
#         if  j.__contains__(i):
#             result.append(i)
#             break
#
print(result)