def solution(strings, n):
    A = []  # n번째 문자를 저장할 리스트
    mapping = {}  # 문자와 원본 문자열을 매핑할 딕셔너리
    
    # n번째 문자를 리스트 A에 추가하고, 딕셔너리에 저장
    for word in strings:
        key = word[n]
        A.append(key)
        mapping[word] = key
    
    # 리스트 A를 정렬
    A.sort()
    
    # 정렬된 A를 기준으로 원래 문자열을 정렬
    sorted_strings = sorted(strings, key=lambda x: (mapping[x], x))
    
    return sorted_strings