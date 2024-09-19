def solution(a, b):
    answer = str(a)+str(b)
    answer1 = int(answer)
    answer = str(b)+str(a)
    answer2 = int(answer)
    if answer1 > answer2:
        return answer1
    else:
        return answer2
