'''
Integer or String
Description

You have been using ast.literal_eval() to take input in a suitable format. Have you thought of how does it distinguish between different data types and data structures? We will solve a similar but smaller problem here. You will be given a string as input. You just have to determine if the string can be an integer or no?
This is also encountered a lot in Data Science. Upon taking a lot of data, sometimes integer values are treated as a string, and due to that a lot of functionalities of integer data which you will learn ahead are rendered useless.

'''


string = '12.1'
flag=0

for char in string:
    if not char.isdigit():
        print('STR')
        flag=1

if flag == 0:
    print('INT')
