def solution(n):
    def prime_factors(n):
        factors = []
        # 2로 나누기
        while n % 2 == 0:
            if 2 not in factors:
                factors.append(2)
            n //= 2
        
        # 3 이상의 홀수로 나누기
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if i not in factors:
                    factors.append(i)
                n //= i
        
        # n이 소수인 경우 추가
        if n > 2:
            factors.append(n)
        
        return factors
    
    return prime_factors(n)