def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer2 = answer / len(arr)
    return answer2