def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        total = 0
        for j in range(1, i+1):
            if i % j == 0 :
                total += 1
        
        if total % 2 == 0:
            answer += i
        elif total % 2 != 0:
            answer -= i
    return answer