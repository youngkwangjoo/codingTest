def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        x = i[s:s+l]
        y = int(x)
        if y > k:
            answer.append(y)
    return answer