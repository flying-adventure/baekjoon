def solution(brown, yellow):
    # 노란색의 (가로X+세로Y)*2 + 4 = 갈색 , 가로+세로=K
    #XY=노란색 개수
    K=(brown-4)//2
    ans=[]
    Y=1
    while True:
        if yellow%Y==0 and yellow//Y+Y==K:
            ans.append(K-Y+2)
            ans.append(Y+2)
            break
        Y+=1
        
                

    return ans