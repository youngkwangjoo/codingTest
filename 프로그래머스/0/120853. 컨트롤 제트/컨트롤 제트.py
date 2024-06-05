def solution(s):
    num = s.split() 
    answer = []  
    for i in num:
        if i == "Z":
            if answer: 
                answer.pop() 
        else:
            answer.append(int(i)) 
    return sum(answer)