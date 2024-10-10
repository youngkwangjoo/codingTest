def solution(myString):
    answer1 = []
    answer = myString.split("x")
    for i in answer:
        if i:
            answer1.append(i)
    answer1.sort()
    return answer1