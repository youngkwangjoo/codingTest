def solution(money):
    americano = 5500
    x, y =  divmod(money, 5500)
    answer = [x, y]
    return answer