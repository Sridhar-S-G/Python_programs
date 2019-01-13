'''Reverse Last X Characters

The program must accept a string value S and an integer X as the input. The program must reverse the last X characters in
S. Then the program must print the modified string as the output.

Boundary Condition(s):
1 <= Length of S <= 100
1 <= X <= Length of S

Input Format:
The first line contains the values of string S.
The second line contains the integer X.

Output Format:
The first line contains the modified string.
Example Input/Output 1:

Input:
skillrack
3

Output:
skillrkca

Explanation:
The last 3 characters in the string "skillrack" are a, c and k. After reversing the last three characters, the string becomes
"skillrkca".
Hence the output is skillrkca

Example Input/Output 2:
Input:
program
7
Output:
margorp '''

solution code:

s=input()
d=int(input())
f=s[:-d-1]
g=s[-d-1:]
g=g[::-1]
f=f+g 
print(f)
