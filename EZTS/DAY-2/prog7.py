#program to check armstrong or not
n=int(input("enter the number"))
rev=0
sum=0
while n>0:
    digit=n%10
    if digit==0:
        rev+=1
    n//=10
    sum+=digit**rev
if sum==n:
    print("it is armstrong")
else:
    print("it is not armstrong")
    
