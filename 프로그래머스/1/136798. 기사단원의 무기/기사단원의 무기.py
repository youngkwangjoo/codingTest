def solution(number, limit, power):
    total = 0
    for i in range(1, number + 1):
        count = count_divisors(i)
        if count > limit:
            total += power
        else:
            total += count
    return total

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count
