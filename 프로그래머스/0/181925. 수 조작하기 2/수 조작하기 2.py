def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        result = numLog[i]-numLog[i-1]
        if result == 1:
            answer += "w"
        elif result == -1:
            answer += "s"
        elif result == 10:
            answer += "d"
        else:
            answer += "a"
    return answer