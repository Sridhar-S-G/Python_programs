'''
The program must accept an integer N as the input. The program must print the binary representation of the square of each
integer from 1 to N as the output.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains the integer N.
Output Format:
The first line contains the binary representation of squares from 1 to N are separated by space(s).
Example Input/Output 1:
Input:
4
Output:
1 100 1001 10000
Explanation:
The square of 1 is 1. So the binary representation of 1 is 1.
The square of 2 is 4. So the binary representation of 4 is 100.
The square of 3 is 9. So the binary representation of 9 is 1001.
The square of 4 is 16. So the binary representation of 16 is 10000.
Hence the output is 1 100 1001 10000
Example Input/Output 2:
Input:
9
Output:
1 100 1001 10000 11001 100100 110001 1000000 1010001
'''
#Solution 
n=int(input())
for i in range(1,n+1):
  print(bin(i**2)[2:],end=' ')
