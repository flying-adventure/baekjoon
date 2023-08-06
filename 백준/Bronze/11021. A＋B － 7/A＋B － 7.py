case_num=int(input())
cnum=1
             
while case_num>0:
    num = list(map(int, input().split()))
    print(f"Case #{cnum}: {num[0]+num[1]}")
    cnum+=1
    case_num-=1