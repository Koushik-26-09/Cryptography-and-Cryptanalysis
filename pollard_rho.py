from  math import gcd
def f(x):
    return (x**2 +1)
def polllard_rho(n,x1):
    x=x1
    xx=f(x)
    p=gcd(x-xx,n)
    while p==1:
        x=f(x)
        xx=f(xx)
        xx=f(xx)
        p=gcd(x-xx,n)
    if p==n:
        return -1
    else:
        return p
n=int(input("Enter the factoring number: "))
x1=int(input("enter the intial value: "))
result=polllard_rho(n,x1)
print(result)