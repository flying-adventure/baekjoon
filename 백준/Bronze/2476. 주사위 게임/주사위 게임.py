person = []

N = int(input())
for i in range(N):
               a,b,c = map(int,input().split())
               if a==b==c:
                   price=10000+a*1000
                   person.append(price)
               elif a==b or a==c :
                   price=1000+a*100
                   person.append(price)
               elif c == b:
                   price=1000+b*100
                   person.append(price)
               else:
                   price = max(a,b,c)*100
                   person.append(price)
price_max=max(person)
print(price_max)               
               
               
               
    