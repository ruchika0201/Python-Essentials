'''
Cheapest Item
Description
You will be given a dictionary with keys as items and values as their prices. You have to print the cheapest item.

Sample input:
A single line non-empty dictionary

Sample output:
cheapest_item name: cheapest_item_cost

'''
import ast

# d = ast.literal_eval(input())
d = {'mobile1':10000, 'mobile2':11000, 'mobile3':13000, 'mobile4':9000, 'mobile5':15000, 'mobile6':16000, 'mobile7':17000, 'mobile8':18000, 'mobile9':19000}
sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=False)
print(sorted_d)
dict_list = list(sorted_d)
print(str(dict_list[0][0]) + ':' + str(dict_list[0][1]))

