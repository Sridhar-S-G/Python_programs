'''
Problem Statement
A string will be given as input, the program must extract the numbers from the string and display as output

Example 1:
Input: Tony Stark's daughter says 143 3000
Output: 143 3000

Example 2:
Input: There4 I think you will be satis5ed with this tutorial
Output: 4 5
'''

#Solution Code
import re
s=input()
results= re.findall(r'\d+',s)
print(*results)
