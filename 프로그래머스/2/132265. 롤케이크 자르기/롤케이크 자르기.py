from collections import Counter
def solution(topping):
    result=0
    part1=Counter(topping)
    part2=set()
    for t in topping:
        part2.add(t)
        part1[t]-=1
        #0개 됐을때 part1에서 빼는게 중요할 듯..
        if part1[t]==0:
            del part1[t]
        if len(part1)==len(part2):
            result+=1
    return result
        
    