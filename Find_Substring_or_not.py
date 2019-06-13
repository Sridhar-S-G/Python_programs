#Problem Statement:
#Enter a string and another word to check whether the word is substring of entered string

#Note: Use the Compiler in interactive mode
#Example:
'''Enter a String: SridharSG
   Enter a word to check it is a substring: Sri
   
   Yes the word Sri word is a substring Sridhar'''
   
   
#Solution Code:
s=input('Enter a String: ')
word=input('Enter a word to check it is a substring: ')
if (s.find(word))!=-1:
    print('\nYes the word %s word is a substring %s'%(word,s))
else:
    print('\nNo the word %s is not a substring %s'%(word,s))
