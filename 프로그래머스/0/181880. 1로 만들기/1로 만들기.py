def solution(num_list):
    k=0
    for i in num_list:
        while i!=1:
            if i%2==0:
                i=i//2
                k+=1
            else:
                i=(i-1)//2
                k+=1
            
    return k
        
            
        