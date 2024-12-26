def solution(food):
    result = [food[0]]  
    for i in food[1:]:  
        if i % 2 == 0:  
            result.append(i)
        else:  
            result.append(i - 1)
    answer = ''  
    for idx, val in enumerate(result[1:], start=1):  
        answer += str(idx) * (val // 2) 
    
    answer = answer + '0' + answer[::-1]
    return answer