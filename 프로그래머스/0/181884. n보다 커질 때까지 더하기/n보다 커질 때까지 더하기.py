def solution(numbers, n):
    x=0
    for i in numbers:
        if x<=n:
            x+=i
        
    return x