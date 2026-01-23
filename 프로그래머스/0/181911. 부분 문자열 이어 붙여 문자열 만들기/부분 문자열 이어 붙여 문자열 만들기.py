def solution(my_strings, parts):

        return "".join(a[s:e+1]for a,(s,e)in zip(my_strings, parts))