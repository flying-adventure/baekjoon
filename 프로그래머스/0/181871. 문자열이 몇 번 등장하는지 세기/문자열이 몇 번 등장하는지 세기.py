def solution(myString, pat):
    k=0
    for i in range(len(myString)):
        k+=myString[i:i+len(pat)].count(pat)
    return k