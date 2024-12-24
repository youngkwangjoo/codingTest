def solution(t, p):
    pl = len(p)
    pi = int(p)
    
    answer = 0
    for i in range(len(t) - pl +1):
        answer2 = t[i:i+pl]
        if int(answer2) <= pi:
            answer += 1
    return answer