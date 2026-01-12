def solution(ineq, eq, n, m):
    if n>m:
        if ineq==">":
            return 1
        else:
            return 0
    if n<m:
        if ineq=="<":
            return 1
        return 0
    if n==m:
        if eq=="=":
            return 1
        else:
            return 0