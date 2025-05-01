def solution(a, d, included):
    answer = 0
    answer1 = []
    for i in range(len(included)):
        x = a + (d * i)
        answer1.append(x)
        if included[i] == True:
            answer += answer1[i]
    return answer