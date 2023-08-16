one=0
zero=0

for _ in range(0,int(input())):
    vote = int(input())
    if vote == 1:
        one+=1
    if vote == 0:
        zero+=1
        
        
if one > zero:
    print("Junhee is cute!")
elif one < zero:
    print("Junhee is not cute!")