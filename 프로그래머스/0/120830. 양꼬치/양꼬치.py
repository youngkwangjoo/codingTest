def solution(n, k):
    answer = ()
    #n은 양꼬치, 12000 k는 음료수 2000, n이 10이되면 -2000
    if n < 10:
        answer = (n*12000) + (k*2000) 
    elif n >= 10:
        answer = (n*12000) +(k*2000) - (n//10*2000)
    return answer