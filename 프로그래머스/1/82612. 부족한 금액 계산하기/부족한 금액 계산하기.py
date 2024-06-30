def solution(price, money, count):
    num = 0
    #3으로 시작해서 빼야할값은 money이고 count만큼 
    for i in range(1, count+1):
        num += i * price
        answer = num-money
    return max(answer, 0)