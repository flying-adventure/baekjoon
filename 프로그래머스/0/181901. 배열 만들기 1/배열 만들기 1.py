def solution(n, k):
    return [k*x for x in range(1,n+1) if k*x<=n]