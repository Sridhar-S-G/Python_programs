'''
Problem:
Print a separator that separates upper traingle and lower triangle

Test Case1:
Input:
5
Output:
* * * * * 
* * * * # 
* * * # * 
* * # * * 
* # * * * 

Test Case2:
Input:
8
Output:
* * * * * * * * 
* * * * * * * # 
* * * * * * # * 
* * * * * # * * 
* * * * # * * * 
* * * # * * * * 
* * # * * * * * 
* # * * * * * * 

'''

# Note: Before refering the below code try to solve by yourself

# Solution


n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i+j==n:
            print('#',end=' ')
        else:
            print('*',end=' ')
    print()
