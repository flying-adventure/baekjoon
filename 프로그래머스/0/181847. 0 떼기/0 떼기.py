def solution(n_str):
    p=0
    for a in n_str:
        if a == '0':
            p+=1

        else:
            return n_str[p:]
        