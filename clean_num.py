'''
Clean Numbers
Description
While extracting data from different sources, often numeric values come in string format and with commas like 1,000 or 23,321 and also sometimes with spaces in start and beginning of the string. For simplicity, we will consider only integer values imbedded with commas. You will take the input and print the cleaned integer without commas and spaces.

'''


string = '4,68,72,352'
output = ''

for char in string:
    if char.isdigit():
        output += char
     
print(int(output))   
