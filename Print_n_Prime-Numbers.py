n=int(input()) #specify the n value till you want the prime number to be printed
flag=0
for i in range(2,n+1):
    for j in range(1,i+1):
        if(i%j==0):
            flag+=1
    if(flag==2):
        print(i) #this line prints output one below another,to print on same line separated by space use 'print(i,end=' ')'
    flag=0
