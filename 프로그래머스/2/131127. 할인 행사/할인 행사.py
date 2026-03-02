from collections import Counter
def solution(want, number, discount):
    peo_want=Counter({w:n for w,n in zip(want,number)})
    
    result=0
    for i in range(len(discount)-9):

        cnt=Counter(discount[i:i+10])
        if all(peo_want[n]<=cnt[n] for n in want):
            result+=1
        
        
    return result