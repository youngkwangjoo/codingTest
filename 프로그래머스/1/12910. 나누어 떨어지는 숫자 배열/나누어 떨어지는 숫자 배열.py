def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        answer.sort()
    if not answer:  # answer 리스트가 비어있는지 확인
        return [-1]

    return answer