'''First and Last Three Bits

Problem Statement:

The program must accept an integer N as the input. The program must the decimal equivalent of the first three bits and the last
three bits in the binary representation of N as the output.
Boundary Condition(s):
4 <= N <= 10^8
Input Format:
The first line contains the value of N.
Output Format:
The first line contains the decimal equivalent of the first three bits and the last three bits separated by a space.
Example Input/Output 1:
Input:
86
Output:
5 6
Explanation:
The binary representation of 86 is 1010110.
The decimal equivalent of the first three bits (101) in the binary presentation of 86 is 5.
The decimal equivalent of the last three bits (110) in the binary presentation of 86 is 6.
Hence the output is 5 6
Example Input/Output 2:
Input:
7
Output:
7 7
'''
#Solution

n=int(input())
b=bin(n)
k=b[2:5]
l=b[-3:]
print(int(k,2),end=' ')
print(int(l,2))
