def solution(str_list, ex):
    ans=[i for i in str_list if not ex in i]
    return "".join(ans)