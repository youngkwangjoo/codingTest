def solution(arr):
    result = []
    for num in arr:
        if num >= 50 and num % 2 == 0:  # 50보다 크거나 같은 짝수인 경우
            result.append(num // 2)
        elif num < 50 and num % 2 != 0:  # 50보다 작은 홀수인 경우
            result.append(num * 2)
        else:
            result.append(num)  # 그 외의 경우는 그대로 유지
    return result
