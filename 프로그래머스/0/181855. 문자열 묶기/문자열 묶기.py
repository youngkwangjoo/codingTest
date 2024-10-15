def solution(strArr):
    answer = []
    length_count = {}  # 길이를 카운트할 딕셔너리

    # 각 문자열의 길이를 저장하고, 길이별로 등장 횟수 카운트
    for i in strArr:
        length = len(i)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    
    # 길이별로 가장 많이 등장한 횟수를 반환
    return max(length_count.values())
