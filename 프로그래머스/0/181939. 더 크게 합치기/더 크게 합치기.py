def solution(a, b):
    answer = 0
    if str(a)+str(b)>=str(b)+str(a):
        return int(str(a)+str(b)) 
    else:
        return int(str(b)+str(a))
    
