import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
intervals = input_list[0]
date = input_list[1]
count = 0
for interval in intervals:
    start = int(interval[0])
    end = int(interval[1])
    if(date == start or date == end or date in range(start, end)):
        count += 1

print(count)