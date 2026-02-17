def solution(rank, attendance):
    members=[]
    for i,x in enumerate(attendance):
        if x == True:
            members.append(rank[i])
    members_s=sorted(members)[0:3]

    ans=0
    for i,x in enumerate(rank):
        if x==members_s[0]:
            ans+=10000*i
        if x==members_s[1]:
            ans+=100*i
        if x==members_s[2]:
            ans+=i
            
    return ans
    
    