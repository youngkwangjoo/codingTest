def solution(numbers, n):
    answer = 0
    result = []
    for i in numbers:
        if answer <= n:
            answer += i
        else:
            return answer
    return answer