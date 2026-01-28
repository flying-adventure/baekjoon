def solution(my_string):
    ans=[0]*52
    for ch in my_string:
        if 'A'<=ch<='Z': 
            ans[ord(ch)-65]+=1
        if 'a'<=ch<='z':
            ans[ord(ch)-65-6]+=1
    return ans