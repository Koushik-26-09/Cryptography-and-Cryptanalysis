from math import gcd
def pollard(n,b):
    a=2
    for j in range(2,b+1):
        a=pow(a,j,n)
    result=gcd(a-1,n)
    if result!=1:
        return result
    else:
        return -1
n=int(input("Enter a factoring number: "))
b=int(input("ENter the Bound: "))
result=pollard(n,b)
print(result)