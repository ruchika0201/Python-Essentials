'''
Consider a nested dictionary as follows:

{'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}

Your task is to flatten a nested dictionary and join the nested keys with the "_" character. For the above dictionary, the flattened dictionary would be as follows:

{'Fruit': 1, 'Vegetable_Cabbage': 2, 'Vegetable_Cauliflower': 3, 'Spices': 4}

The input will have a nested dictionary.

The output should have two lists. The first list will have keys and the second list should have values. Both lists should be sorted.

Sample Input:

{'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}

Sample Output:

['Fruit', 'Spices', 'Vegetable_Cabbage', 'Vegetable_Cauliflower']
[1, 2, 3, 4]

'''

my_dict = dict({'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4})
output_dict = {}
for key, value in my_dict.items():
    if(type(value) is not dict):
        output_dict[key] = value
    else:
        for temp_key, temp_value in value.items():
            output_dict[key + '_' + temp_key] = temp_value

key_list = []
value_list = []

for key, value in output_dict.items():
    key_list.append(key)
    value_list.append(value)
    

print(key_list)
print(value_list)
