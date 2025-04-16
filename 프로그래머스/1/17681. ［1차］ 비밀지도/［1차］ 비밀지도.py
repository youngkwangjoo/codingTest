def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer2 = i | j
        answer2 = bin(answer2)[2:].zfill(n)
        answer2 = answer2.replace("0"," ").replace("1","#")
        answer.append(answer2)
    return answer