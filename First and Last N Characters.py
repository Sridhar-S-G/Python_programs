'''                                               First and Last N Characters

Problem Statement:

The program must accept a string S contains only alphabets and an integer N as the input. The program must print the first N alphabets in the string and then print the last N alphabets in the string as the output.
Boundary Condition(s):
2 <= Length of S <= 100
1 <= N <= Length of S

Input Format:
The first line contains the string S.
The second line contains the integer N.

Output Format:
The first line contains the first N alphabets and the last N alphabets .

Example Input/Output 1:                                       
Input:                                                         
Engineering
3

Output:
Enging

Explanation:
The first 3 alphabets in the string "Engineering" are E n g.
The last 3 alphabets in the string "Engineering" are i n g. 
Hence the output is Enging

firstfirst


'''
#Solution

s=input()
n=int(input())
if(n==len(s)):
  print(s,end='')
  print(s)
else:
  a=s[:n]
  b=s[-n:]
  c=a+b
  print(c)


