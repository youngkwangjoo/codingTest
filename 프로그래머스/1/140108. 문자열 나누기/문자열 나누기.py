def solution(s):
    answer = 0
    x_count = 0
    not_x_count = 0
    x = ''
    
    for i, ch in enumerate(s):
        if x_count == 0:
            x = ch  # 새로운 분리 시작
        if ch == x:
            x_count += 1
        else:
            not_x_count += 1
        
        if x_count == not_x_count:
            answer += 1
            x_count = 0
            not_x_count = 0

    if x_count > 0 or not_x_count > 0:
        answer += 1  # 남은 것들도 하나로 처리
    
    return answer
