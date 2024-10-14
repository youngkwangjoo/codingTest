import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2 // math.gcd(denom1, denom2)
    #x는 몇 증가했는지 알려줌
    x = denom // denom1
    y = denom // denom2
    a = numer1 * x + numer2 *y
    result = math.gcd(a,denom)
    answer = [a//result, denom//result]
    return answer