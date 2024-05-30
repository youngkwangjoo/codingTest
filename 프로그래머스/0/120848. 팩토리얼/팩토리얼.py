def solution(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i  
        if answer > n:
            return i -1
    return n

#x값에 따른 팩토리얼이 나옴
#1, 2, 6, 24, 120, 840 
