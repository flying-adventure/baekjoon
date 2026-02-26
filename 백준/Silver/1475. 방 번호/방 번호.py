from collections import Counter
N=list(str(input()))
cnt=Counter(N)
num=[]
k=0
for i,x in cnt.items():
    if i=="6" or i=="9":
        k+=x
        x=0
        
    num.append(x)
num.append((k+1)//2)
print(max(num))

    
    

