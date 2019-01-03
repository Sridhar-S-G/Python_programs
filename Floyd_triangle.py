'''
Problem statement:

Print floyd triangle in the pattern as given below

input:
3

output:
0
01
012 
'''

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print('')
