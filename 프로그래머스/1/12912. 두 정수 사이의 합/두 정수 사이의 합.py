def solution(a, b):
    answer = 0
    max_min = [a, b]
    for i in range(min(max_min), max(max_min)+1):
        answer += i
    return answer