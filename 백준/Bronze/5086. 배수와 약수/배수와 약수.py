while True:
    a, b = map(int,input().split())
    
    if a==0 and b==0:
        break
    k=0
    #배수 찾기
    i=1
    while a>=b*i:
        if a == b*i:
            print("multiple")
            k+=1
        i+=1
    #약수 찾기
    p = 1
    while b>=a*p:
        if b == a*p:
            print("factor")
            k+=1
            
        p+=1
    #둘 다 아닌 경우
    if k == 0 :
        print("neither")
            
        