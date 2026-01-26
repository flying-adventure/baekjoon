def solution(my_string, s, e):
    ed=my_string[s:e+1]
    return my_string[:s]+ed[::-1]+my_string[e+1:]