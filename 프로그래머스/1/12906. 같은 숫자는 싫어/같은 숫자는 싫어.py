def solution(arr):
    answer = [arr[0]]
    
    # 리스트의 요소를 순회하며 비교
    for i in range(1, len(arr)):
        # 연속된 요소가 다르면 결과 리스트에 추가
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    
    return answer
