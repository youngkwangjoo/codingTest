def solution(arr):
    answer = []
    if 2 not in arr:
        return [-1]
    fi = arr.index(2)
    li = len(arr) -1 - arr[::-1].index(2)
    
    answer = arr[fi:li+1]
    return answer