def solution(name, yearning, photo):
    year_dic={}
    for a,b in zip(name,yearning):
        year_dic[a]=b
    result=0
    ans=[]
    
    for photos in photo:
        for peo in photos:
            if peo in year_dic:
                result+=year_dic[peo]
        ans.append(result)
        result=0
            
    return ans