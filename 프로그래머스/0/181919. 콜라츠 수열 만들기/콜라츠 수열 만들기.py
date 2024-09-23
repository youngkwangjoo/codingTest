def solution(n):
    answer = [n]  # 초기값 n을 수열에 포함

    while n != 1:
        if n % 2 == 0:  # n이 짝수인 경우
            n //= 2
        else:  # n이 홀수인 경우
            n = 3 * n + 1
        answer.append(n)  # 계산된 n을 수열에 추가
    return answer