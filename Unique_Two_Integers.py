'''
Unique Two Integers
The program must accept N integers as the input. The program must print yes as the output if every two integers are
unique. Else the program must print no as the output.
Note: N is always even.
Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 10^8
Input Format:
The first line contains N.
The second line contains N integers separated by space.
Output Format:
The first line contains yes or no
Example Input/Output 1:
Input:
4
39 622 64 39
Output:
yes
Explanation:
The integers 39 and 622 are unique.
The integers 64 and 39 are also unique.
So the output is yes.
Example Input/Output 2:
Input:
6
12 65 23 14 45 45
Output:
no
Explanation:
The last two integers 45 and 45 are not unique so no is printed.
'''
#Solution
n=int(input())
l=list(map(int,input().split()))
st,en,f=0,2,1
while(n!=0):
  sub_list=l[st:en]
  if(sub_list[0]!=sub_list[1]):
    st+=2
    en+=2
    n-=2
  else:
    f=0
    break
if(f==0):
  print('no')
else:
  print('yes')
