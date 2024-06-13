'''
Write a program to accept a 4 digit number from user and count 0, even and odd number
'''
n = input('Enter a number 4 digit number::')
print(n)
count_0 = 0;
count_even = 0;
count_odd = 0;

if(n.isdigit() and len(n) == 4):
    print('It is a 4 digit number')
    num_str = str(n)
    for i in range(0,4):
        x = int(num_str[i]);
        if x == 0:
            count_0+=1
        elif x%2 == 0:
            count_even+=1
        else:
            count_odd+=1
            
    print(str(count_0) + '\n' + str(count_even) + '\n' + str(count_odd))
            
    

