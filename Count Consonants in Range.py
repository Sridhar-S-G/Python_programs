''' 
The program must accept two alphabets ch1 and ch2 as the input. The program must print the count of consonants
between the given alphabets (including ch1 and ch2) as the output.
Input Format:
The first line contains ch1 and ch2 separated by a space.
Output Format:
The first line contains the count of consonants between ch1 and ch2.
Example Input/Output 1:
Input:
d j
Output:
5
Example Input/Output 2:
Input:
s u
Output:
2
'''

#Solution Code
a=['a','e','i','o','u']
b='abcdefghijklmnopqrstuvwxyz'
d=0
c=input()
for i in range(b.index(c[0]),b.index(c[2])+1):
  if b[i] not in a:
    d+=1
print(d)
