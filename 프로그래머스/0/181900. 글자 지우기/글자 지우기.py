def solution(my_string, indices):
    indices=sorted(indices,reverse=True)
    for a in indices:
        my_string=my_string[:a]+my_string[a+1:]
    return my_string