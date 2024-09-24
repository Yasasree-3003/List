'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10
'''
input_line = input()
my_list = []
number = ""
for char in input_line:
    if char == " ":
        if number:
            my_list.append(int(number))
            number = ""
    else:
        number += char
if number:
    my_list.append(int(number))
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i], end=" ")
print()
