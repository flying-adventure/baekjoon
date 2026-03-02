def solution(elements):
    #원형 수열 -> 그냥 수열 두 번 연결하기
    ans=set()
    elementss=elements[:]+elements[:]
    for i in range(len(elements)):
        for j in range(len(elements)):
            ans.add(sum(elementss[i:i+j+1]))
        
        
    return len(ans)
    
    