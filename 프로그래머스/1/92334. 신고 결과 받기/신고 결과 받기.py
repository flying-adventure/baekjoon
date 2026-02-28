def solution(id_list, report, k):
    report=set(report)
    
    report_cnt={id:0 for id in id_list}
    user_reports = {id: [] for id in id_list}
    
    for re in report:
        a,b=re.split()
        report_cnt[b]+=1
        user_reports[a].append(b)
    answer=[]
    
    for user in id_list:
        mail_count=0
        for i in user_reports[user]:
            if report_cnt[i]>=k:
                mail_count+=1
        answer.append(mail_count)
            
    return answer