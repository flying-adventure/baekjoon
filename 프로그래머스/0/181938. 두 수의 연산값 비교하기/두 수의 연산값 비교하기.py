def solution(a, b):
    ab=str(a)+str(b)
    ab2=2*a*b
    if int(ab)>=ab2:
        return int(ab)
    else:
        return ab2