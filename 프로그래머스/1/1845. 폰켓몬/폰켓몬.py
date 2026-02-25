from collections import Counter
def solution(nums):
    cnt=Counter(nums)
    k=0
    for i in cnt.keys():
        k+=1
    
    return min(k,len(nums)//2)
    