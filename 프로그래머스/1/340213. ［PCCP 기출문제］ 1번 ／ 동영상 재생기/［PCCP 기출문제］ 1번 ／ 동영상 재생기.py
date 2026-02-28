def solution(video_len, pos, op_start, op_end, commands):
    
    ss_l=60*int(video_len[0:2]) + int(video_len[3:])
    ss_s=60*int(op_start[0:2]) + int(op_start[3:])
    ss_e=60*int(op_end[0:2]) + int(op_end[3:])
    ss=60*int(pos[0:2]) + int(pos[3:])
    if ss<=ss_e and ss>=ss_s:
            ss=ss_e
    for i in commands:
        if i=='prev':
            if ss<10:
                ss=0
            else:
                ss-=10
                
        elif i=='next':
            
            if ss_l-ss<10:
                ss=ss_l
            else:
                ss+=10
               
                
        if ss<=ss_e and ss>=ss_s:
            ss=ss_e
        
    mm=str(ss//60)
    ss=str(ss%60)
    if len(ss)==1:
        ss='0'+ss
    if len(mm)==1:
        mm='0'+mm
    ans=[mm,":",ss]
    return "".join(ans)
        
        