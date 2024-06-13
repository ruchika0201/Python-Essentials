'''
Description
Find Extra Character
Description
Given two strings, one of the strings will contain an extra character. Find the extra character. The number of all the other characters in both the strings will be the same. Check the sample input/output for more clarification.

The code will be case sensitive.

'''



def formDict(string, dict1):
    for alpha in string:
        if alpha not in dict1:
            dict1[alpha] = 1
        
        else:
            dict1[alpha] += 1
    

if __name__ == '__main__':
    str1 = 'abcd'
    str2 = 'cedab'
    dict1 = {}
    formDict(str1, dict1)
    formDict(str2, dict1)
    for key, value in dict1.items():
        if value % 2 != 0:
            print(key)
    

