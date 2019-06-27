'''
Print the pattern like given below

Sample Test Case1
Input:
5
Output:
* * * * 1 
* * * * 2 
* * * * 3 
* * * * 4 
5 
4 * * * * 
3 * * * * 
2 * * * * 
1 * * * * 

Sample Test Case2
Input:
6
Output:
* * * * * 1 
* * * * * 2 
* * * * * 3 
* * * * * 4 
* * * * * 5 
6 
5 * * * * * 
4 * * * * * 
3 * * * * * 
2 * * * * * 
1 * * * * * 

'''

# Note: Before going into solution try the solve by your own 

# Solution:

n=int(input())
c=0
for i in range(1,((n-1)*2)+2):
    for j in range(1,((n-1)*2)+2):
        if j==n and i<=n:
            c+=1
            print(c,end=' ')
        elif j==n and i>n:
            c-=1
            print(c,end=' ')
        elif i>n and j>n or i<n and j<n:
            print('*',end=' ')
    print()
