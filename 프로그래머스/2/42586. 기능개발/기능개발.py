
def solution(progresses, speeds):
    days=[]
    for p,s in zip(progresses,speeds):
        remain=100-p
        d=(remain+s-1)//s
        days.append(d)
    day=days[0]
    ans=[]
    cmt=1
    
    for i in days[1:]:
        if day>=i:
            cmt+=1
        else:
            ans.append(cmt)
            day=i
            cmt=1
    ans.append(cmt)
    return ans
            
            
        
    return days
        