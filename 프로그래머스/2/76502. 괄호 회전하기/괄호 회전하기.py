def right(s):
    stack = []
    pair = {')': '(', '}': '{', ']': '['}
    
    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)      
        else: # 닫힌 괄호면
            # 스택이 비어있거나(처음부터 닫힌게 옴), 짝이 안 맞으면 False
            if not stack or stack.pop() != pair[i]:
                return False
    return len(stack) == 0    
def solution(s):
    #이거 원형 순열이랑 비슷하지 않나?
    ss=s*2
    result=0
    for i in range(len(s)-1):
        sss=ss[i:i+len(s)]
        if right(sss):
            result+=1
    return result
