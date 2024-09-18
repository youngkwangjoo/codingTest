def solution(a, b):
    answer = [a,b]
    answer2 = 2*a*b
    answer3 = int("".join(map(str,answer)))
    if answer2 > answer3:
        return answer2
    else:
        return answer3