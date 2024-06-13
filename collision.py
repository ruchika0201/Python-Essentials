import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
M1 = input_list[0]#measurements of meteor 1
M2 = input_list[1]#measurements of meteor 2
point_1_rad = M1[0]
x1 = M1[1]
y1 = M1[2]

point_2_rad = M2[0]
x2 = M2[1]
y2 = M2[2]

sum_of_rad = abs(point_2_rad + point_1_rad)
# print('Dist between radii is ' + str(sum_of_rad))

dist = int(((x2-x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
# print('Dist between points is '+ str(dist))

if(dist <= sum_of_rad):
    print('Collision!')
else:
    print('No Collision')