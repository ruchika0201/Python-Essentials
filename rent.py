'''

You are moving to a new city for an internship for a few
months and have to rent a house for that purpose.
You have to pay the full month's house rent even if you have
lived for a few days for that month. i.e. if you start on 15th
Jan and leave by 15th May, you still have to pay full rent for
months of Jan and May too.
Your task is to find the months that you have to pay rent for
so that you can write post-dated cheques to your landlord.
You will be given two dates as input and your task is to print
all months between the dates including the months the
dates are from
The input will contain the two dates in a list as follows:
[2017,1,1,2017,3,4] which corresponds to 1st Jan, 2017 and
4th March, 2017. This date is in the format(yyyy,mm,dd)
(the code for taking input has already been written for you,
please don't modify that)
The output should contain a list with names of months you
have to pay the rent for(the list should be sorted
chronologically based on months, i.e May should come
before August). You can assume that there won't be more
than 12 months between two dates.
You'll need to use the datetime module for this problem
which can be referred to here. You can choose to use any
other method too.
Sample Input:
[2017,1,1, 2017, 1,1]
Sample Output:
['January']


'''

from datetime import date

day1= [2023, 1, 1] # 1 January 2023
day2 = [2023, 5, 5] # 5 May 2023

day_1 = date(day1[0], day1[1], day1[2])
day_2 = date(day2[0], day2[1], day2[2])

output = []
start = day_1

while(start <= day_2):
    output.append(start.strftime('%B'))
    
    if start.month == 12:
        start = start.replace(year=start.year +1, month=1)
    else:
        start = start.replace(year=start.year, month=start.month+1)
    
sorted(output)

print(output)