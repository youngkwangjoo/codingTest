def solution(n):
    answer1 = []  

    for num in range(2, n + 1): 
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            answer1.append(num)  # 소수면 추가

    return len(answer1)  # 소수 목록 반환
