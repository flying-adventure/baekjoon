def solution(code):
    mode=0
    ret=[]
    for i,x in enumerate(code):
        if x=="1":
            mode=1-mode
            continue
        if mode==0:
            if i%2==0:
                ret.append(x)
        if mode==1:
            if i%2!=0:
                ret.append(x)
    ans="".join(ret)
    return ans if ans else "EMPTY"

            
                