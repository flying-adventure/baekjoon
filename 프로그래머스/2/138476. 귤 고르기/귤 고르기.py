from collections import Counter
def solution(k, tangerine):
    counter=Counter(tangerine)
    freq=[]
    for x in counter.values():
        freq.append(x)
    freq.sort(reverse=True)
    total=0
    kinds=0
    for c in freq:
        total += c
        kinds += 1
        if total >= k:
            return kinds
    