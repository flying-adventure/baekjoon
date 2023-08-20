for _ in range(int(input())):
    a = input()
    sc = 0 
    t = 0    
    for i in a:
        if i == "O":
            t+=1
        else:
            t=0
        sc += t
        
    print(sc)
        
    
        
        
     
