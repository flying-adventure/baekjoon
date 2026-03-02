def solution(arr1, arr2):
    row1,col1=len(arr1),len(arr1[0])
    row2,col2=len(arr2),len(arr2[0])
    #결과 행렬은 항상 앞 행렬의 세로*뒷행렬의 가로 크기가 된다.
    answer = [[0] * col2 for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
    
    