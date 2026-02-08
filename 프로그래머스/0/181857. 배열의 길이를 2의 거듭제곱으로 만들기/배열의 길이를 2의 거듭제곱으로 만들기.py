def solution(arr):
    arrlist=[1,2,4,8,16,32,64,128,256,512,1024]
    for i in arrlist:
        if i-len(arr)>=0:
            for k in range(i-len(arr)):
                arr.append(0)
            break
    return arr
    