from itertools import combinations
from collections import Counter
def solution(orders, course):
    ans=[]
    for i in course:
        menu_l=[]
        for j in orders:
            for comb in combinations(sorted(j),i):
                menu_l.append(comb)
        cnt=Counter(menu_l)
        if cnt:
            max_val = max(cnt.values())

            if max_val >= 2:
                for menu, count in cnt.items():
                    if count == max_val:
                        ans.append("".join(menu))

    return sorted(ans)