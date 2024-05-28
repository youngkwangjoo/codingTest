def solution(order):
    answer = 0
    x = str(order)
    for i in x:
        if i in "369":
            answer += 1
    return answer