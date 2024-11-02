def solution(picture, k):
    answer = []
    for one in picture:
        result = ""
        for two in one:
            two = two * k
            result += two
        for _ in range(k):  # 세로로 k번 반복하여 answer에 추가
            answer.append(result)
            
    return answer