def solution(myStr):
    ans=[]
    for i in myStr.split("a"):
        for p in i.split("b"):
            for k in p.split("c"):
                if k:
                    ans.append(k)
    return ans if ans else ["EMPTY"]
        
