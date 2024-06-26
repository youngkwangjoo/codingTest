def solution(n):
    answer = ["수"]
    
    for i in range(1,n):
        if i % 2 == 0:
            answer.append("수")
        elif i % 2 != 0:
            answer.append("박")
    return "".join(answer)