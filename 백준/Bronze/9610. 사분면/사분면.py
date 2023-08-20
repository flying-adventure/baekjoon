a,b,c,d,e = 0,0,0,0,0
for _ in range(int(input())):
    t,f=map(int,input().split())
    if t==0 or f==0:
        e+=1
    if t>0:
        if f>0:
            a+=1
        if f<0:
            b+=1
    if t<0:
        if f>0:
            c+=1
        if f<0:
            d+=1
print("Q1: " + str(a))
print("Q2: " + str(c))
print("Q3: " + str(d))
print("Q4: " + str(b))
print("AXIS: " + str(e))

        