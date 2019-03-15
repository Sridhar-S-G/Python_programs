'''
Count of Special Characters

The program must accept a string S as the input. The program must print the count of special characters in the string S as
the output.
Note: Special character is a character which is not an alphabet or not a digit.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains the string S.
Output Format:
The first line contains the count of special characters in S.
Example Input/Output 1:
Input:
eur09!^rp!e*!1*
Output:
6
Example Input/Output 2:
Input:
o$ra^nge*
Output:
3
'''
d,a=0,0
s=input()
for i in s:
  if(i.isalpha()):
    a+=1
  if(i.isdigit()):
    d+=1
print(len(s)-a-d)
