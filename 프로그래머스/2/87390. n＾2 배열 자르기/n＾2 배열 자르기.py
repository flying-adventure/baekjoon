def solution(n, left, right):
    
    #col열row행부터 right-left개의 수열
    ans=[]
    for x in range(left,right+1):
        col=x%n
        row=x//n
        ans.append(max(col,row)+1)
    return ans
        
    
            
        