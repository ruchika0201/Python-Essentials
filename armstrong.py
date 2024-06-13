'''
Armstrong number Description Any number, say n is called an Armstrong number if it is equal to the sum of its digits, where each is raised to the power of number of digits in n.
For example:
153=13+53+33


'''

n = int(input("Enter a number: "))
n_string = str(n)
length = len(n_string)
count = 0 
for i in range(0, length):
    num = int(n_string[i])
    count += num ** length
print(count)
