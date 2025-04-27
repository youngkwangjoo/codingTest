from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # 제곱근까지만 검사
        if n % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    for comb in combinations(nums, 3):  # 3개를 뽑는 모든 조합
        if is_prime(sum(comb)):          # 3개를 더한 값이 소수인지 확인
            count += 1
    return count
