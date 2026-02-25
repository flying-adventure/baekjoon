def solution(sizes):
    mxs=[]
    #길이가 긴 변을 한 쪽으로 통일
    for a,b in sizes:
        if a>b:
            mxs.append((a,b))
        else:
            mxs.append((b,a))
    print(list(mxs))
    mx,my = max(mxs, key=lambda x: x[0])[0], max(mxs, key=lambda x: x[1])[1]
    
    
    return mx*my