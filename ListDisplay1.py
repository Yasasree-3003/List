'''
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
'''
size = int(input())
my_list = []
for i in range(size):
    element = int(input())
    my_list.append(element)
for i in range(size):
    if i < size - 1:
        print(my_list[i], end=" ")
    else:
        print(my_list[i])
