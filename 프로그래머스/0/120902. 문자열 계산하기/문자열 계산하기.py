def solution(my_string):
    num = my_string.split()  # 공백을 기준으로 문자열을 분리
    answer = int(num[0])     # 첫 번째 숫자를 결과로 초기화

    # for 문을 사용하여 연산자와 숫자를 순차적으로 처리
    for i in range(1, len(num) - 1, 2):
        operator = num[i]
        next_number = int(num[i + 1])

        if operator == '+':
            answer += next_number
        elif operator == '-':
            answer -= next_number

    return answer