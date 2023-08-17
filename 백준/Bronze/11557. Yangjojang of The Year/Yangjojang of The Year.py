T = int(input())


for _ in range(T):
    univ = ""
    mdri = 0
    for _ in range(int(input())):
        uni, dri = input().split()
        dri=int(dri)
        if(dri > mdri):
            mdri = dri
            univ = uni
        
            
    print(univ)