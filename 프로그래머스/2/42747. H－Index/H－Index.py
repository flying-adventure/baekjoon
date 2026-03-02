from collections import Counter
def solution(citations):
    #n편 중 h번 이상 인용된 논문이 h편 이상, 나머지는 h번 이하 인용
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i]>=i+1:
            continue
        else:
            return i
    return len(citations)
            
    
    