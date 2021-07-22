# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    
    # Write your logic here
    if (year%100)==0:
        if(year%400)==0:
            leap = True
        else:
            leap = False
    elif (year%4)==0:
        leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))