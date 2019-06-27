'''
Problem 

Print the black slash in the pattern given below

Test case1
Input:
8
Output:
\        
 \       
  \      
   \     
    \    
     \   
      \  
       \ 

Test case2
Input:
5
Output:
\     
 \    
  \   
   \  
    \ 
    
'''

# Note: Before refering the solution try to solve the problem 

# Solution 

n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print('\\',end=' ')
        else:
            print(' ',end='')
    print()
