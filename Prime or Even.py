'''
The program must accept an integer N as the input. The program must print valid if N is a prime number or an even
number. Else the program must print invalid as the output.
Boundary Condition(s):
1 <= N <= 10^5
Input Format:
The first line contains the integer N.
Output Format:
The first line contains either valid or invalid.
Example Input/Output 1:
Input:
53
Output:
valid
Explanation:
The integer 53 is a prime number.
Hence the output is valid
Example Input/Output 2:
Input:
100
Output:
valid
Explanation:
The integer 100 is an even number.
Hence the output is valid
Example Input/Output 3:
Input:
27
Output:
invalid'''

#Solution
n=int(input())
f=0
for i in range(1,n+1):
  if n%i==0:
    f+=1
if (f==2 or n%2==0):
  print('valid')
else:
  print('invalid')
