def solution(before, after):
    after = list(after)  # 문자열을 리스트로 변환
    for i in before:
        if i in after:
            after.remove(i)  # 특정 값을 제거
        else:
            return 0
    # after 리스트가 비어 있는지 확인
    if len(after) == 0:
        return 1
    else:
        return 0