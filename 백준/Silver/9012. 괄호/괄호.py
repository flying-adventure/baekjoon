def is_vps(vps):
    count = 0
    for ch in vps:
        if ch == "(":
            count += 1
        else:  # ")"
            count -= 1
        
        if count < 0:
            return "NO"
    
    if count == 0:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    s = input().strip()
    print(is_vps(s))
