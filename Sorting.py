'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
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
my_list.sort()
for i in range(len(my_list)):
    print(my_list[i], end=" ")
print()
