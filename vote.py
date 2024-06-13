
'''
Vote for Food
Description
Your team is going for camping and you are taking a vote to decide what food to pack for dinner.
Everyone gets a vote and the food item that gets at least one more than half of the votes wins. None of the items wins if nothing gets at least one more than half votes. Assume that every person gets only one vote.
The input will contain a list of food items where each occurrence of an item represents one vote. You should print the winning food item as output. If there is no clear winner, print "NOTA".

Sample Input:
["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]
Sample Output:
pasta
'''


import ast,sys
input_str = sys.stdin.read()
votes_temp = ast.literal_eval(input_str)
votes = ["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]
n = int(len(votes) / 2 + 1)
my_dict = {}
for i in votes:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

sorted(my_dict, key= lambda item: item[1], reverse=True)
first_element = list(my_dict.items())[0]
if(first_element[1] >= n):
    print(first_element[0])
else:
    print('NOTA')
