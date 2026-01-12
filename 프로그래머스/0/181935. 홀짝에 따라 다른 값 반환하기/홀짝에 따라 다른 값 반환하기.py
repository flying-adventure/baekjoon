def solution(n):
    if n % 2 == 1:
        k = (n + 1) // 2
        return k * k
    else:
        m = n // 2
        return 4 * m * (m + 1) * (2 * m + 1) // 6
