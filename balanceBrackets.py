string=input()
stack = []
n = len(string)
for i in range(0, n):
    if(string[i] == '(' or string[i] == '{' or string[i] == '['):
        stack.append(string[i])
        print('stack appended '+ str(stack))
    else:
        s = stack.pop()
        if (string[i] == ')' and s != '(') or \
           (string[i] == ']' and s != '[') or \
           (string[i] == '}' and s != '{'):
               break
if not stack:
    print('Balanced')
else:
    print('Unbalanced')