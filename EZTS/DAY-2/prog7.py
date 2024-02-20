#program to check armstrong or not
n=int(input("enter the number"))
n=n1
order=len(str(n))
sum=0
while n>0:
    digit=n%10
    n//=10
    sum+=digit**order
if sum==n1:
    print("it is armstrong")
else:
    print("it is not armstrong")
    
