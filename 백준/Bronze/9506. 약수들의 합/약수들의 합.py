while True:
    n = int(input())
    mint = []
    if n == -1:
        break
    #어케함??? ㅋ
    for i in range(1,n):
        if n%i == 0:
            mint.append(i)
    if sum(mint) == n:
        print(n," = ", " + ".join(str(i) for i in mint), sep="")
    else:
        print(n,"is NOT perfect.")
        
