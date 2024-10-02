def solution(binomial):
    result = binomial.split()
    
    # 문자열을 숫자로 변환
    num1 = int(result[0])
    num2 = int(result[2])
    
    # 연산자에 따라 처리
    if result[1] == "-":
        answer = num1 - num2
    elif result[1] == "+":
        answer = num1 + num2
    else:
        answer = num1 * num2
    
    return answer
