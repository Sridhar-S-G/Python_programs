'''
Problem Statement:

The program must accept a string S as the input. The program must toggle the case of vowels in the string S. Then the
program must print the modified string as the output.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains the string S.
Output Format:
The first line contains the modified string.
Example Input/Output 1:
Input:
EquilIbriUm
Output:
eqUIlibrIum
Explanation:
The vowels in the string "EquilIbriUm" are 'E', 'u', 'i', 'I', 'i' and 'U'.
So toggle the case of all the vowels in the string "EquilIbriUm".
Hence the output is eqUIlibrIum
Example Input/Output 2:
Input:
JUNKVIRUS
Output:
JuNKViRuS  '''

#Solution

s=input()
v=['a','e','i','o','u','A','E','I','U']
for i in s:
    if i in v:
        if(i.isupper()==1):
            print(i.lower(),end='')
        else:
            print(i.upper(),end='')
    else:
        print(i,end='')


