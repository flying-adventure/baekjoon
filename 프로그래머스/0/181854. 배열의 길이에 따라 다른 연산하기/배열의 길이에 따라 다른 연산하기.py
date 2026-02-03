def solution(arr, n):
    if len(arr)%2==1:
        return [x+n if i%2==0 else x for i,x in enumerate(arr)]
    if len(arr)%2==0:
        return [x+n if i%2==1 else x for i,x in enumerate(arr)]
        


        
    