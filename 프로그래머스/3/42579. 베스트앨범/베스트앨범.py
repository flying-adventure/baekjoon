def solution(genres, plays):
    #장르별 재생 수 총합
    total={}
    #장르별 곡 목록 songs={genres:[plays,idx]}
    songs={}
    
    for i, (g,p) in enumerate(zip(genres,plays)):
        total[g]=total.get(g,0)+p
        if g not in songs:
            songs[g]=[]
        songs[g].append((p,i))
    genre_order=sorted(total,key=lambda x: -total[x])
    ans=[]
    for g in genre_order:
        songs[g].sort(key=lambda x:(-x[0]))
        ans.extend(i for _,i in songs[g][:2])
    return ans