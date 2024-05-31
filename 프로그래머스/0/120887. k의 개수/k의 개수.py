def solution(i, j, k):
    answer = 0
    numbers = list(range(i, j + 1))
    numbers_str = ''.join(map(str, numbers))
    x = ','.join(numbers_str)
    ks = str(k)
    answer = numbers_str.count(ks)
    return answer