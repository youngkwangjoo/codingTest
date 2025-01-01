def solution(a, b, n):
    answer = 0  # 받은 콜라의 총 개수

    while n >= a:
        new_cola = (n // a) * b  # 받을 수 있는 콜라 병 수
        answer += new_cola  # 총 받은 콜라 병 수에 추가
        n = new_cola + (n % a)  # 받은 콜라 병과 남은 빈 병 수를 합산

    return answer