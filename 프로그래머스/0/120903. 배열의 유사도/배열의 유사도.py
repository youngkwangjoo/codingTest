def solution(s1, s2):
    # 두 배열을 집합으로 변환하여 중복을 제거하고 공통 원소를 구합니다.
    set1 = set(s1)
    set2 = set(s2)
    
    # 공통 원소의 개수를 반환합니다.
    return len(set1.intersection(set2))