'''
The program must accept an alphabet CH as the input. The program must print all the consonants from CH circularly as the
output.
Note: CH is always in lowercase.
Boundary Condition(s):
'a' <= CH <= 'z'
Input Format:
The first line contains CH.
Output Format:
The first line contains all the consonants in lowercase from CH circularly.
Example Input/Output 1:
Input:
w
Output:
wxyzbcdfghjklmnpqrstv
Explanation:
All the lowercase consonants are printed circularly starting from the given alphabet w
Example Input/Output 2:
Input:
e
Output:
fghjklmnpqrstvwxyzbcd
'''

Solution
def patternizer(patternizer_key):
    conso='bcdfghjklmnpqrstvwxyz'
    if patternizer_key in conso:
        return(present(patternizer_key,conso))
    else:
        return (absent(patternizer_key,conso))

def present(patternizer_key,conso):
    s=[]
    for i in range(conso.index(patternizer_key),21):
        s.append(conso[i]) 
    for i in range(0,conso.index(patternizer_key)):
        s.append(conso[i]) 
    return(s)
    
def absent(patternizer_key,conso):
    s=[]
    for i in range(conso.index(chr(ord(patternizer_key)+1)),21):
        s.append(conso[i])
    for i in range(0,conso.index(chr(ord(patternizer_key)+1))):
        s.append(conso[i])
    return(s)
    
patternizer_key=input()
print(*patternizer(patternizer_key),sep='')
