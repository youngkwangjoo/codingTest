def solution(angle):
    if angle <= 90:
        answer = (angle // 90)+1
    elif angle < 180 and angle > 90:
        answer = (angle // 90)+2
    else:
        answer = (angle // 90)*2
    return answer