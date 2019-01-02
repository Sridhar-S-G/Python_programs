a = int(input()) #enter 1st number
b = int(input()) #enter 2nd number

if(a > b):
    m = a
else:
    m = b

while(1):
    if(m % a == 0 and m % b == 0):
        print(m)
        break;
    m = m + 1
