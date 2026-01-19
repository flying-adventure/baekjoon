def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        best = None
        for x in arr[s:e+1]:
            if x > k:
                if best is None or x < best:
                    best = x
        answer.append(best if best is not None else -1)
    return answer
