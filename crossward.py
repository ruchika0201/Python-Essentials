'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

str1 = 'cdw'
str2 = 'crossward'
j = 0
    
    # Iterate through each letter in the word
for letter in str2:
        # If the letter matches the current letter in the crossword, move to the next crossword letter
    if j < len(str1) and letter == str1[j]:
        j += 1
        
        # If we reach the end of the crossword without matching all letters in the word, return "no"
    if j == len(str1):
        break
    
    # If we have matched all letters in the word, return "yes", otherwise return "no"
if j == len(str1):
    print("Yes")
else:
    print("No")
    
