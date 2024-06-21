def solution(array):
    answer = sorted(array)
    x = len(answer) // 2 
    answer = answer[x]
    return answer