def solution(arr):
    
    k=0
    while True:
        prev=arr.copy()
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i]//=2
            if arr[i]<50 and arr[i]%2==1:
                arr[i]=arr[i]*2+1
        if prev==arr:
            return k
        k+=1
            