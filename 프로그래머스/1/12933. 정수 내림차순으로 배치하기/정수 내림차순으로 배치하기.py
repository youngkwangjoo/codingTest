def solution(n):
    answer = list(str(n))
    answer.sort(reverse = True)
    answer2 = int("".join(answer))
    return answer2