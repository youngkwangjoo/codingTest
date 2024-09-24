def solution(myString):
    answer = ''
    for i in myString:
        if i == "a":
            answer += "A"
        elif i == "A":
            answer += "A"
        elif i.isupper():
            answer += i.lower()  # 대문자인 경우 소문자로 변환
        else:
            answer += i  # 그 외에는 그대로 추가
    return answer
