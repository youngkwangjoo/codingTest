def solution(array, commands):
    answer = []
    for a in commands:
        i,j,k = a
        answer2 = array[i-1:j]
        answer2.sort()
        answer.append(answer2[k-1])
    return answer