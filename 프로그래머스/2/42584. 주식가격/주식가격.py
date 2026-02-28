def solution(prices):
    t=0
    l=len(prices)
    result=[0]*l
    stack=[]
    for i in range(l):
        while stack and prices[stack[-1]]>prices[i]:
            j=stack.pop()
            result[j]=i-j
        stack.append(i)
        
    while stack:
        j=stack.pop()
        result[j]=l-1-j
    return result