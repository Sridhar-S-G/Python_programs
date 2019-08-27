a,b=map(int,input().split())
lim,gcd=0,0
if(a>b):lim=b
else:lim=a
for i in range(1,lim):
    if(a%i==0 and b%i==0):
        if(gcd<i):
            gcd=i
print(gcd)
