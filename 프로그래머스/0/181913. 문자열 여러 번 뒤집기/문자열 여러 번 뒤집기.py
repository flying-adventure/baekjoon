def solution(my_string, queries):
    s = my_string
    for x, y in queries:
        s = s[:x] + s[x:y+1][::-1] + s[y+1:]
    return s
