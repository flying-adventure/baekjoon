def solution(num_list):
    odd = sum(n for i,n in enumerate(num_list) if i%2==1)
    even = sum(n for i,n in enumerate(num_list) if i%2==0)
    
    return max(odd,even)