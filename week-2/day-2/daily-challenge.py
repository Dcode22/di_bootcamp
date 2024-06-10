# Challenge 1
num = int(input("Enter a number: "))
length = int(input("Enter a length: "))

num_list = []

for i in range(1, length +1):
    num_list.append(num * i)
print(num_list)


#Challenge 2
user_string = input("Enter a string: ")
user_string_copy = user_string
for i in range(1, len(user_string_copy)):
    if user_string_copy[i -1] == user_string_copy[i]:
        user_string = user_string[:i] + ' ' + user_string[i+1:]
user_string = user_string.replace(" ", "")
print('user_string stripped duplicates:', user_string)
