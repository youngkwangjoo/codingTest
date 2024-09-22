def solution(myString):
    answer = ''
    for i in myString:
        if i < 'l':  # 'l'보다 알파벳 순서에서 앞서는지 확인
            answer += 'l'
        else:
            answer += i
    return answer
