'''
Write a program that computes the value of n+nn+nnn+nnnn+... nn...n ntimes with a given number as the value of n.

For example, if n=3 , then you have to find the value of 3+33+333

if n=10, then you have to find the value of 10 + 1010 + 101010 + 10101010 + 1010101010 + 101010101010 + 10101010101010 + 1010101010101010 +101010101010101010+ 10101010101010101010

Note: n will always be a positive number


'''

n = int(input("Enter a number: "))
n_string = str(n)
count = 0 

for i in range(1, n+1):
    temp = n_string * i
    num = int(temp)
    count = count + num
    
print(count)
    

