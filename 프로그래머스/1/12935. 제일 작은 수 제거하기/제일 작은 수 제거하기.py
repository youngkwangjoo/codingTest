def solution(arr):
    answer = []
    x = min(arr)
    if len(arr) <= 1:
        return [-1]

    for i in arr:
        if i != x:
            answer.append(i)
    return answer
    