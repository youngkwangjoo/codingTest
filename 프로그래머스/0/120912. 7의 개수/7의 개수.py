def solution(array):
    answer = 0
    num = []
    for i in array:
        for x in str(i):
            num.append(int(x))
            answer = num.count(7)
    return answer