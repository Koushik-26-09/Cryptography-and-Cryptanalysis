def shanks(g,h,p):
    m=int(p**0.5)+1
    baby_steps={}
    for i in range(m):
        baby_steps[pow(g,i,p)]=i
    current=h
    g_in=pow(g,-m,p)
    for i in range(m+1):
        if current in baby_steps:
            return i*m+baby_steps[current]
        current=(current*g_in)%p
    return -1
p=23
g=5
h=8
result=shanks(g,h,p)
print(result)