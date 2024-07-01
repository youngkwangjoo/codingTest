#유클리드 호제법...
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(a, b):
    gcd_value = gcd(a, b)
    lcm_value = (a * b) // gcd_value
    return [gcd_value, lcm_value]