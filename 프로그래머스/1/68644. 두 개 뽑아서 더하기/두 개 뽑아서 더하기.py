def solution(numbers):
    # 결과를 저장할 set
    result = set()
    
    # 모든 가능한 두 수의 조합을 더하여 결과에 추가
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum_value = numbers[i] + numbers[j]
            result.add(sum_value)
    
    # set을 리스트로 변환한 후 오름차순으로 정렬
    return sorted(result)

# 테스트 예시
print(solution([2, 1, 3, 4, 1]))  # [2, 3
