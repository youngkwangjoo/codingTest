def solution(phone_number):
    # 인덱스 [-1]부터 [-5]까지의 부분을 추출
    end_part = phone_number[-1:-5:-1][::-1]
    
    # 나머지 부분을 '*'로 변환
    masked_part = '*' * (len(phone_number)+1 - 5)
    
    # 두 부분을 결합하여 반환
    return masked_part + end_part