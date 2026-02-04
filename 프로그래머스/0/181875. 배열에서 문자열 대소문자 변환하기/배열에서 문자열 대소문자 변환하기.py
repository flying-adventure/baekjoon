def solution(strArr):
    for i,x in enumerate(strArr):
        if i%2==1:
            strArr[i]=strArr[i].upper()
        if i%2==0:
            strArr[i]=strArr[i].lower()
    return strArr