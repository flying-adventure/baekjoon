limit= int(input())
num_l=1

while num_l <= limit:
    num= list(map(int, input().split()))
    print(f"Case #{num_l}: {num[0]} + {num[1]} = {num[0]+num[1]}")
    num_l+=1
    
