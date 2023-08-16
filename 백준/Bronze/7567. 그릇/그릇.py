bowl = input()

high=10

if bowl[0]==bowl[1]:
    high+=5
else:
    high+=10
    
for i in range(2,len(bowl)):
    if bowl[i-1] == bowl[i]:
        high+=5
    else:
        high+=10
print(high)
    