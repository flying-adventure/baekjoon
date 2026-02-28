def solution(survey, choices):
    per={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}

    for i,s in zip(survey,choices):
        a,b=i
        if s>=4:
            per[b]+=s-4
        if s<4:
            per[a]+=4-s
    result=[]
    types = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for first, second in types:
        if per[first] >= per[second]:
            result.append(first)
        else:
            result.append(second)
            
    return "".join(result)