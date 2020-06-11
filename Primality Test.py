import math
t=int(input())
for i in range(t):
    n=int(input())
    p=False
    if n==1:
       print("no",end='\n')
    else:
       for i in range(2,int(math.sqrt(n))):
           if n%i==0:
              p=True
              break
       if p==True:
            print("no",end='\n')
       else:
            print("yes",end='\n')

