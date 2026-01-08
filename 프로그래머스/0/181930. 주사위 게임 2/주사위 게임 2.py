def solution(a, b, c):
    ssum= a+b+c
    msum=a*a+b*b+c*c
    dsum=a*a*a+b*b*b+c*c*c
    
    if a==b==c:
        return ssum*msum*dsum
    if a==b or a==c or b==c:
        return ssum*msum
    else:
        return ssum
        